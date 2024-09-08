import json
from pathlib import Path

def main():
	root_path: Path = Path().resolve()
	print(f"INFO: root_path: '{root_path}'")
	#relative_path: Path = Path(__file__).parent.resolve()
	#print(f"INFO: relative_path: '{relative_path}'")

	path_to_format = Path(root_path / "src/I4/rules")
	for path in Path(path_to_format).rglob("*.json"):
		if path.stem != "sources":
			with open(path, 'r') as f:
				data = json.load(f)
			with open(path, 'w') as f:
				json.dump(data, f, indent="\t")

	print(f"STATUS: Done.")

if __name__ == "__main__":
	main()
