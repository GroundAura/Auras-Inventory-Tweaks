import copy
import json
from pathlib import Path

from auralib.config import read_config

def actual_path(path: str | Path, cwd_var: str, root_path: str | Path = Path().resolve()) -> Path:
	return Path(path.replace(cwd_var, str(root_path)))

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

def main():
	# Set path variables
	root_path: Path = Path().resolve()
	print(f"INFO: root_path: '{root_path}'")
	relative_path: Path = Path(__file__).parent.resolve()
	print(f"INFO: relative_path: '{relative_path}'")
	config_path: Path = Path(relative_path) / 'generate-i4.ini'

	# Read settings config
	config_settings: dict[str, any] = read_config(config_path, preserve_key_case=True)
	print(f"INFO: config_settings: '{config_settings}'")
	cwd_var: str = config_settings["PATH"]['sCWDVariable']
	sources_path: Path = actual_path(config_settings["PATH"]['sPathSources'], cwd_var, root_path)
	templates_path: Path = actual_path(config_settings["PATH"]['sPathTemplates'], cwd_var, root_path)
	schema_var: str = config_settings["SCHEMA"]["sSchemaVariable"]
	default_schema: str = config_settings["SCHEMA"]["sDefaultSchema"]
	override_schema: bool = config_settings["SCHEMA"]["bOverrideSchema"]
	indentation: str = config_settings["FORMATTING"]["sIndent"].replace("\\t", "\t")
	try:
		indentation = int(indentation)
	except ValueError:
		pass

	# Read rule sources
	sources: dict[str, str] = {}
	with open(sources_path, 'r') as f:
		sources: dict = json.load(f)
	for key in sources:
		sources[key] = actual_path(sources[key], cwd_var, root_path)

	# Read rules
	rulesets: dict[str, list[dict[str, dict[str, any]]]] = {}
	for key, source_dir in sources.items():
		rulesets[key] = []
		for path in Path(source_dir).rglob("*.json"):
			with open(path, 'r') as f:
				rules = json.load(f)["rules"]
				rulesets[key].extend(rules)

	# Read templates
	templates: dict[str, dict[str, any]] = {}
	for template in templates_path.rglob("*.ini"):
		templates[template.name] = read_config(template, preserve_key_case=True)["SETTINGS"]
	# Format templates
	for _, template in templates.items():
		rule_list = template["lRules"]
		if len(rule_list) == 1 and "," in rule_list[0]:
			# Fix list formatting
			rule_list = rule_list[0]
			template["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list.split(",")]
		elif "\'" in rule_list[0] or "\"" in rule_list[0]:
			# Fix string formatting
			template["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list]
		template["sPathColorTheme"] = actual_path(template["sPathColorTheme"], cwd_var, root_path)
		template["sPathOutput"] = actual_path(template["sPathOutput"], cwd_var, root_path)
		if template["sSchema"] in (None, "", schema_var) or override_schema:
			template["sSchema"] = default_schema

	# Read colors
	themes: dict[str, dict[str, any]] = {}
	for _, template in templates.items():
		themes[template["sPathColorTheme"].stem] = read_config(template["sPathColorTheme"], preserve_key_case=True, inline_comment_prefixes=(";", "//"))["COLORS"]
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
	i4_template: dict[str, any] = {
		"$schema": default_schema,
		"rules": []
	}
	outputs: dict[str, dict[str, any]] = {}
	for template_key, template in templates.items():
		#print(template)
		output: dict[str, any] = {"path": template["sPathOutput"], "contents": copy.deepcopy(i4_template)}
		# Add rules
		for ruleset in template["lRules"]:
			output["contents"]["rules"].extend(rulesets[ruleset])
		# Update colors
		for rule in output["contents"]["rules"]:
			rule = update_icon_color(rule, themes[template["sPathColorTheme"].stem])
		outputs[template_key] = output

	# Write output
	for _, output in outputs.items():
		with open(output["path"], "w") as f:
			json.dump(output["contents"], f, indent=indentation)

	print(f"STATUS: Done.")

if __name__ == '__main__':
	main()
