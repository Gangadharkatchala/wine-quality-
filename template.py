# it create repositoty automatically
import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define project name and list of files to create
project_name = "my_project"
list_of_files = [
    f"GK/{project_name}/__init__.py",
    f"GK/{project_name}/components/__init__.py",
    f"GK/{project_name}/utils/__init__.py",
    f"GK/{project_name}/utils/common.py",
    f"GK/{project_name}/config/__init__.py",
    f"GK/{project_name}/config/configuration.py",
    f"GK/{project_name}/pipeline/__init__.py",
    f"GK/{project_name}/entity/__init__.py",
    f"GK/{project_name}/entity/config_entity.py",
    f"GK/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "paramas.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
]

# Create files and directories
for file_path in list_of_files:
    # Use pathlib's Path object for better handling of paths
    file_path = Path(file_path)
    
    # Extract directory and filename
    filedir, filename = os.path.split(file_path)
    
    # Create directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    # Create the file if it doesn't exist or is empty
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w') as f:
            # Add default content based on file type
            if filename.endswith('.py'):
                f.write("# This is a Python file\n")
            elif filename.endswith('.yaml'):
                f.write("# This is a YAML file\n")
            elif filename.endswith('.html'):
                f.write("<!-- This is an HTML file -->\n")
            else:
                f.write("# This is a file\n")
        logging.info(f"Creating file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")
