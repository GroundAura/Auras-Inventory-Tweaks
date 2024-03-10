import configparser
import os
# import regex

ROOT_PATH = os.getcwd()
CONFIG_PATH = os.path.join(ROOT_PATH, "src\\I4\\templates\\AIO.ini")

def read_config(file_path):
	config = configparser.ConfigParser(comment_prefixes=(";", "#", "//"), inline_comment_prefixes=(";", "#", "//"))
	config.read(file_path)
	return config

def exclude_directories(dirs, exclude_list):
	# if not exclude_list:
	# 	exclude_list = ['']
	return [d for d in dirs if d not in exclude_list]

def concatenate_json_files_from_directory(starting_directory, excluded_dirs):
	combined_content = ""
	prefix_to_remove = "{\n\"$schema\": \"https://raw.githubusercontent.com/GroundAura/InventoryInjector/main/docs/InventoryInjector.schema.json\",\n\"rules\": [\n"
	suffix_to_remove = "\n]\n}"
	for root, dirs, files in os.walk(starting_directory):
		dirs[:] = exclude_directories(dirs, excluded_dirs)
		for file in files:
			if file.endswith('.json'):
				with open(os.path.join(root, file), 'r') as f:
					combined_content = f.read()
					combined_content = combined_content.removeprefix(prefix_to_remove)
					combined_content = combined_content.removesuffix(suffix_to_remove)
					combined_content += "\n"
	return combined_content

def fix_json_formatting(text):
	text = text.replace("\n\n", "\n")
	text = text.replace("}\n\t{", "},\n\t{")
	text = text.replace("},\n]", "}\n]")
	# text = text.replace("", "")
	return text

# def fix_json_indent(text)
# 	text = text.replace("{\n\t", "\t{\n\t")
# 	return text

def main():
	print(f"Trying to read config file from: {CONFIG_PATH}")
	config = read_config(CONFIG_PATH)
	if not config:
		print("config not found or failed to read")
		return

	template_file = os.path.join(ROOT_PATH, config.get('GENERAL', 'TEMPLATE_FILE'))
	output_file = os.path.join(ROOT_PATH, config.get('GENERAL', 'OUTPUT_FILE'))

	with open(template_file, 'r') as f:
		output = f.read()

	excluded_dirs = ['']

	for section in config.sections():
		if section != "GENERAL" and 'SOURCE_FOLDER' in config[section]:
			print(f"GENERATE SECTION: {section}")
			source_folder = os.path.join(ROOT_PATH, config[section]['SOURCE_FOLDER'])
			concatenated_content = concatenate_json_files_from_directory(source_folder, excluded_dirs)
			block_name = f"[{section}]"
			output = output.replace(block_name, concatenated_content)
			output = fix_json_formatting(output)

	with open(output_file, 'w') as f:
		f.write(output)

if __name__ == "__main__":
	main()
