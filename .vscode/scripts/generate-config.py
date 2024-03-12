import configparser
import os

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
	# suffix_to_remove = "\n"
	for root, dirs, files in os.walk(starting_directory):
		dirs[:] = exclude_directories(dirs, excluded_dirs)
		for file in files:
			if file.endswith('.ini'):
				with open(os.path.join(root, file), 'r') as f:
					# combined_content = f.read()
					combined_content += f.read() + "\n"
					# combined_content = combined_content.removesuffix(suffix_to_remove)
	return combined_content

def fix_formatting(text):
	text = text.replace("\n\n\n\n", "\n\n\n")
	# text = text.replace("", "")
	return text

def main():
	SOURCES_PATH = os.path.join(ROOT_PATH, "src\\SkyUI Config\\sections\\sources.ini")

	print(f"Trying to read config file from: {SOURCES_PATH}")
	config_sources = read_config(SOURCES_PATH, False)
	if not config_sources:
		print("sources config not found or failed to read")
		return

	TEMPLATES_PATH = os.path.join(ROOT_PATH, "src\\SkyUI Config\\templates")
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

				with open(output_file, 'w') as f:
					f.write(output)

if __name__ == "__main__":
	main()
