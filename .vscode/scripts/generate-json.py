import configparser
import os
# import regex

ROOT_PATH = os.getcwd()

def read_config(file_path, case_sensitive):
	config = configparser.ConfigParser(comment_prefixes=(";", "#", "//"), inline_comment_prefixes=(";", "#", "//"))
	if case_sensitive:
		config.optionxform = lambda option: option
	config.read(file_path)
	return config

def exclude_directories(dirs, exclude_list):
	# if not exclude_list:
	# 	exclude_list = ['']
	return [d for d in dirs if d not in exclude_list]

def concatenate_files_from_directory(starting_directory, excluded_dirs):
	combined_content = ""
	prefix_to_remove_1 = "{\n\"$schema\": \"https://raw.githubusercontent.com/GroundAura/InventoryInjector/main/docs/InventoryInjector.schema.json\",\n\"rules\": [\n"
	prefix_to_remove_2 = "{\n\"$schema\": \"https://raw.githubusercontent.com/Exit-9B/InventoryInjector/main/docs/InventoryInjector.schema.json\",\n\"rules\": [\n"
	suffix_to_remove = "\n]\n}"
	for root, dirs, files in os.walk(starting_directory):
		dirs[:] = exclude_directories(dirs, excluded_dirs)
		for file in files:
			if file.endswith('.json'):
				with open(os.path.join(root, file), 'r') as f:
					combined_content = f.read()
					combined_content = combined_content.removeprefix(prefix_to_remove_1)
					combined_content = combined_content.removeprefix(prefix_to_remove_2)
					combined_content = combined_content.removesuffix(suffix_to_remove)
					combined_content += "\n"
	return combined_content

def fix_formatting(text):
	text = text.replace("\n\n", "\n")
	text = text.replace("}\n\t{", "},\n\t{")
	text = text.replace("},\n]", "}\n]")
	# text = text.replace("", "")
	return text

# def fix_indent(text)
# 	text = text.replace("{\n\t", "\t{\n\t")
# 	return text

# def replace_colors(text, config):
# 	for section in config.sections():
# 		for key, value in config.items(section):
# 			# print(f"{key} = #{value}")
# 			text = text.replace(key, "#" + value)
# 			text = text.replace(key, value)

def main():
	SOURCES_PATH = os.path.join(ROOT_PATH, "src\\I4\\rules\\sources.ini")

	print(f"Trying to read config file from: {SOURCES_PATH}")
	config_sources = read_config(SOURCES_PATH, False)
	if not config_sources:
		print("sources config not found or failed to read")
		return

	TEMPLATES_PATH = os.path.join(ROOT_PATH, "src\\I4\\templates")
	excluded_dirs = ['']

	for _, _, files in os.walk(TEMPLATES_PATH):
		for file in files:
			if file.endswith('.ini'):
				TEMPLATE_PATH = os.path.join(TEMPLATES_PATH, file)
				print(f"Trying to read config file from: {TEMPLATE_PATH}")
				config_template = read_config(TEMPLATE_PATH, False)
				if not config_template:
					print("template config not found or failed to read")
					return

				template_file = os.path.join(ROOT_PATH, config_template.get('GENERAL', 'TEMPLATE_FILE'))
				output_file = os.path.join(ROOT_PATH, config_template.get('GENERAL', 'OUTPUT_FILE'))
				color_file = os.path.join(ROOT_PATH, config_template.get('GENERAL', 'COLOR_THEME'))

				print(f"Trying to read config file from: {color_file}")
				config_colors = read_config(color_file, True)
				if not config_colors:
					print("colors config not found or failed to read")
					return

				with open(template_file, 'r') as f:
					output = f.read()

				for section in config_sources.sections():
					if section != "GENERAL" and 'SOURCE_FOLDER' in config_sources[section]:
						print(f"GENERATE SECTION: {section}")
						source_folder = os.path.join(ROOT_PATH, config_sources[section]['SOURCE_FOLDER'])
						concatenated_content = concatenate_files_from_directory(source_folder, excluded_dirs)
						block_name = f"[{section}]"
						output = output.replace(block_name, concatenated_content)
						output = fix_formatting(output)
						# output = replace_colors(output, config_colors)
						for section in config_colors.sections():
							for key, value in config_colors.items(section):
								# print(f"{key} = #{value}")
								output = output.replace(key, "#" + value)

				with open(output_file, 'w') as f:
					f.write(output)

if __name__ == "__main__":
	main()
