import os
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

PROJECT_NAME = "cnnClassifier"

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{PROJECT_NAME}/__init__.py",
    f"src/{PROJECT_NAME}/components/__init__.py",
    f"src/{PROJECT_NAME}/utils/__init__.py",
    f"src/{PROJECT_NAME}/config/__init__.py",
    f"src/{PROJECT_NAME}/config/configuration.py",
    f"src/{PROJECT_NAME}/pipeline/__init__.py",
    f"src/{PROJECT_NAME}/entity/__init__.py",
    f"src/{PROJECT_NAME}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "notebook/trials.ipynb",
    "templates/index.html"
]

# Function to create directories and empty files
def create_file_structure(file_list):
    for filepath in file_list:
        filepath = Path(filepath)
        file_dir, filename = os.path.split(filepath)

        if file_dir != "":
            os.makedirs(file_dir, exist_ok=True)
            logging.info(f"Created directory: {file_dir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created empty file: {filepath}")
        else:
            logging.info(f"{filename} already exists")

# Create the file structure
create_file_structure(list_of_files)
