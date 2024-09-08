import copy
#from copy import deepcopy
import json
#from json import dump as json_dump, load as json_load, loads as json_loads
#import os
#from os import walk, path
#from os.path import join as path_join
from pathlib import Path

from auralib.config import read_config
#from auralib.files import get_root_path

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
	print(root_path)
	relative_path: Path = Path(__file__).parent.resolve()
	print(relative_path)
	config_path: Path = Path(relative_path) / 'generate-i4.ini'

	# Read settings config
	config_settings: dict[str, any] = read_config(config_path, preserve_key_case=True)
	print(config_settings)
	cwd_var: str = config_settings["PATH"]['sCWDVariable']
	#print(type(cwd_var))
	#print(cwd_var)
	sources_path: Path = actual_path(config_settings["PATH"]['sPathSources'], cwd_var, root_path)
	#print(type(sources_path))
	#print(sources_path)
	templates_path: Path = actual_path(config_settings["PATH"]['sPathTemplates'], cwd_var, root_path)
	#print(type(templates_path))
	#print(templates_path)
	schema_var: str = config_settings["SCHEMA"]["sSchemaVariable"]
	#print(schema_var)
	default_schema: str = config_settings["SCHEMA"]["sDefaultSchema"]
	#print(default_schema)
	override_schema: bool = config_settings["SCHEMA"]["bOverrideSchema"]
	#print(override_schema)
	indentation: str = config_settings["FORMATTING"]["sIndent"].replace("\\t", "\t")
	try:
		indentation = int(indentation)
	except ValueError:
		pass
	#indentation: str = "\t"
	#print(indentation == "\t")
	#print(type(indentation) == type("\t"))
	#print(type(indentation))
	#print(indentation)
	#exit()

	# Read rule sources
	sources: dict[str, str] = {}
	with open(sources_path, 'r') as f:
		sources: dict = json.load(f)
	for key in sources:
		sources[key] = actual_path(sources[key], cwd_var, root_path)
	#print(type(sources))
	#print(f"* {next(iter(sources.values()))}")

	# Read rules
	rulesets: dict[str, list[dict[str, dict[str, any]]]] = {}
	for key, source_dir in sources.items():
		#print(f"{key}: '{source_dir}'")
		#for dirpath, _, filenames in os.walk(source_dir):
		#	for filename in filenames:
		#		if filename.endswith('.json'):
		for path in Path(source_dir).rglob("*.json"):
			with open(path, 'r') as f:
				rulesets[key] = json.load(f)["rules"]
			#print(f"* {path}")

	# Debug: Print rulesets
	#print(type(rulesets))
	##print(f"{rulesets}")
	#key, ruleset = next(iter(rulesets.items()))
	#print(f" {type(key)}, {type(ruleset)}")
	##print(f" '{key}'")
	##print(f" {ruleset}")
	#rule = next(iter(ruleset))
	#print(f"  {type(rule)}")
	##print(f"  {rule}")
	#rule_key, rule_data = next(iter(rule.items()))
	#print(f"   {type(rule_key)}, {type(rule_data)}")
	#print(f"   '{rule_key}'")
	#print(f"   {rule_data}")
	#section_key, section_data = next(iter(rule_data.items()))
	#print(f"	{type(section_key)}, {type(section_data)}")
	#print(f"	'{section_key}'")
	#print(f"	{section_data}")
	##for key, ruleset in rulesets.items():
	##	#print(f"\n\n\n'''\n{key}:\n{json.dumps(ruleset, indent=2)}\n'''")

	# Read templates
	templates: dict[str, dict[str, any]] = {}
	#for dirpath, _, filenames in os.walk(templates_path):
	#	for filename in filenames:
	#		if filename.endswith('.ini'):
	for template in templates_path.rglob("_test*.ini"):
		templates[template.name] = read_config(template, preserve_key_case=True)["SETTINGS"]
		#print(f"** {read_config(template, preserve_key_case=True)["GENERAL"]}")
	# Format templates
	for _, template in templates.items():
		#print(template["lRules"])
		#template["lRules"] = [item.strip().strip("'") for item in template["lRules"][0].split(',')]
		#template["lRules"] = ['OTHER', 'WEAPONS', 'ARMOR', 'INGESTIBLES', 'SCROLLS', 'INGREDIENTS', 'BOOKS', 'KEYS', 'MISC', 'SPELLS']
		#if isinstance(template["lRules"], str):
		#else:
		#try:
		#	formatted_list = template["lRules"]
		#	formatted_list = ['OTHER', 'WEAPONS', 'ARMOR', 'INGESTIBLES', 'SCROLLS', 'INGREDIENTS', 'BOOKS', 'KEYS', 'MISC', 'SPELLS']
		#	formatted_list[1]
		#	print("formatted", formatted_list[1])
		#	#template["lRules"][1]
		#except IndexError:
		rule_list = template["lRules"]
		#print(type(template["lRules"]))
		#print(len(rule_list))
		if len(rule_list) == 1 and "," in rule_list[0]:
			rule_list = rule_list[0]
			template["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list.split(",")]
			#print("separated list")
		elif "\'" in rule_list[0] or "\"" in rule_list[0]:
			template["lRules"] = [item.strip().strip("\'").strip("\"") for item in rule_list]
			#print("fixed strings")
		#print(template["lRules"])
		#print(len(template["lRules"]))
		#print(type(template["lRules"]))
		#print(type(template["lRules"][0]))
		#print(type(template["lRules"][1]))
		#print("exit()")
		#exit()
		template["sPathColorTheme"] = actual_path(template["sPathColorTheme"], cwd_var, root_path)
		template["sPathOutput"] = actual_path(template["sPathOutput"], cwd_var, root_path)
		if template["sSchema"] in (None, "", schema_var) or override_schema:
			template["sSchema"] = default_schema

	# Read colors
	themes: dict[str, dict[str, any]] = {}
	for _, template in templates.items():
		#for key, value in template.items():
		#	if key == "sPathColorTheme":
		#		themes[value.stem] = read_config(value, preserve_key_case=True, inline_comment_prefixes=(";", "//"))["COLORS"]
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
	#print(themes)

	# Apply templates
	i4_template: dict[str, any] = {
		"$schema": default_schema,
		"rules": []
	}
	outputs: dict[str, dict[str, any]] = {}
	# combine rulesets based on template settings
	# replace colors in rules based on template settings
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
	#print(outputs)

	# Write output
	for _, output in outputs.items():
		with open(output["path"], "w") as f:
			json.dump(output["contents"], f, indent=indentation)

	print(f"STATUS: Done.")

if __name__ == '__main__':
	main()
