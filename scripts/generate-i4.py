import copy
import json
from pathlib import Path
from typing import Any

from auralib.config import read_config

def actual_path(path: str | Path, cwd_var: str, root_path: str | Path = Path().resolve()) -> Path:
	path = str(path)
	path = path.replace(cwd_var, str(root_path))
	return Path(path)

def read_sources(sources_path: str | Path, root_path: str | Path, cwd_var: str) -> dict:
	with open(sources_path, 'r') as f:
		data: dict = json.load(f)
		for key in data:
			data[key] = data[key].replace(cwd_var, str(root_path))
		return data

def rgb_to_hex(rgb_string: str) -> str:
	# Split the RGB string into its components
	rgb_values: list[str] = rgb_string.split(",")
	# Convert each component from string to integer
	r, g, b = map(int, rgb_values)
	# Convert each component to a two-digit hexadecimal string
	hex_color: str = f"{r:02X}{g:02X}{b:02X}"
	return hex_color

def update_icon_color(d: dict, color_map: dict):
	for key, value in d.items():
		if isinstance(value, dict):
			if key == "iconColor" and "anyOf" in value:
				# Replace values in the "anyOf" list
				value["anyOf"] = [color_map.get(color, color) for color in value["anyOf"]]
			else:
				# Recurse into nested dictionaries
				update_icon_color(value, color_map)
		elif key == "iconColor" and isinstance(value, str):
			# Replace the string value of "iconColor"
			d[key] = color_map.get(value, value)

def write_as_json(path: str, data: dict, indent: int | str | None = "\t") -> None:
	with open(path, 'w') as f:
		json.dump(data, f, indent=indent)

def main() -> None:
	# Set path variables
	root_path: Path = Path().resolve()
	print(f"INFO: root_path: '{root_path}'")
	relative_path: Path = Path(__file__).parent.resolve()
	print(f"INFO: relative_path: '{relative_path}'")
	config_path: Path = Path(relative_path) / 'generate-i4.ini'

	# Read settings config
	config_settings: dict[str, dict[str, Any]] = read_config(config_path, preserve_key_case=True)
	print(f"INFO: config_settings: '{config_settings}'")
	cwd_var: str = config_settings["PATH"]['sCWDVariable']
	sources_path: Path = actual_path(config_settings["PATH"]['sPathSources'], cwd_var, root_path)
	templates_path: Path = actual_path(config_settings["PATH"]['sPathTemplates'], cwd_var, root_path)
	schema_var: str = config_settings["SCHEMA"]["sSchemaVariable"]
	default_schema: str = config_settings["SCHEMA"]["sDefaultSchema"]
	override_schema: bool = config_settings["SCHEMA"]["bOverrideSchema"]
	indentation: str | int = config_settings["FORMATTING"]["sIndent"].replace("\\t", "\t")
	try:
		indentation = int(indentation)
	except ValueError:
		pass
	#default_icon_source: str = config_settings[""][""]
	#default_icon_source: str = "SkyUI/icons_item_psychosteve.swf"

	# Read rule sources
	sources: dict[str, str] = {}
	with open(sources_path, 'r') as f:
		sources: dict = json.load(f)
	for key in sources:
		sources[key] = actual_path(sources[key], cwd_var, root_path)

	# Read rules
	## TODO: add 'invalid json syntax' error handling
	rulesets: dict[str, list[dict[str, dict[str, Any]]]] = {}
	for key, source_dir in sources.items():
		rulesets[key] = []
		for path in Path(source_dir).rglob("*.json"):
			with open(path, 'r') as f:
				rules = json.load(f)["rules"]
				rulesets[key].extend(rules)

	# Read templates
	templates: dict[str, dict[str, Any]] = {}
	for ini in templates_path.rglob("*.ini"):
		templates[ini.name] = read_config(ini, preserve_key_case=True)["SETTINGS"]
	# Format templates
	for _, template_settings in templates.items():
		rule_list: list = template_settings["lRules"]
		if len(rule_list) == 1 and "," in rule_list[0]:
			# Fix list formatting
			rule_list = rule_list[0]
			template_settings["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list.split(",")]
		elif "\'" in rule_list[0] or "\"" in rule_list[0]:
			# Fix string formatting
			template_settings["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list]
		template_settings["sPathColorTheme"] = actual_path(template_settings["sPathColorTheme"], cwd_var, root_path)
		template_settings["sPathOutput"] = actual_path(template_settings["sPathOutput"], cwd_var, root_path)
		if template_settings["sSchema"] in (None, "", schema_var) or override_schema:
			template_settings["sSchema"] = default_schema

	# Read colors
	themes: dict[str, dict[str, str]] = {}
	for _, template_settings in templates.items():
		color_path: Path = template_settings["sPathColorTheme"]
		themes[color_path.stem] = read_config(color_path, preserve_key_case=True, inline_comment_prefixes=(";", "//"))["COLORS"]
	# Format colors
	for _, theme in themes.items():
		for color_key, color_value in theme.items():
			color_value = color_value.replace(" ", "").replace("0x", "")
			if "," in color_value:
				color_value = rgb_to_hex(color_value.lstrip("(").rstrip(")"))
			if color_value == "":
				theme[color_key] = "#FFFFFF"
			elif color_value[0] == "#":
				theme[color_key] = color_value.upper()
			else:
				theme[color_key] = "#" + color_value.upper()

	# Apply templates
	i4_template: dict[str, Any] = {
		"$schema": default_schema,
		"rules": []
	}
	i4_files: dict[str, dict[str, Any]] = {}
	for template_name, template_settings in templates.items():
		#print(template)
		output_path: Path = template_settings["sPathOutput"]
		i4_file: dict[str, Any] = {"path": output_path, "contents": copy.deepcopy(i4_template)}
		# Add rules
		i4_file_rules: list[dict] = i4_file["contents"]["rules"]
		rulesets_to_add: list = template_settings["lRules"]
		for ruleset_name in rulesets_to_add:
			i4_file_rules.extend(rulesets[ruleset_name])
		# Update colors
		for rule in i4_file_rules:
			rule = update_icon_color(rule, themes[template_settings["sPathColorTheme"].stem])
		i4_files[template_name] = i4_file

	# Write output
	for _, i4_file in i4_files.items():
		output_path = i4_file["path"]
		if not Path.exists(output_path) or not Path.is_file(output_path):
			output_path.parent.mkdir(parents=True, exist_ok=True)
			output_path.touch()
		with open(i4_file["path"], "w") as f:
			json.dump(i4_file["contents"], f, indent=indentation)

	print(f"STATUS: Done.")

if __name__ == '__main__':
	main()
