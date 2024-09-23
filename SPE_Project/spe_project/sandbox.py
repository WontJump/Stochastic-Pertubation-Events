

from pathlib import Path

current_directory = Path.cwd()
new_directory = current_directory / "new_folder"
new_directory.mkdir(parents=True, exist_ok=True)
