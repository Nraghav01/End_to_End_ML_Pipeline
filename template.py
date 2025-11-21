#Modular MLOps structure
#This will create the entire project folder structure in one shot -  no need to manually create the folder structure
#In the MLOps lifecycle, the first step after understanding the problem is to structure your project. This is typically done by using a template
import os
from pathlib import Path
import logging
#Logging is a means of tracking events that happen when some software runs. Logging is important for software developing, debugging, and running.
#With logging, you can leave a trail of breadcrumbs so that if something goes wrong, we can determine the cause of the problem.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = "ml_wine_project"

#List of folders and files that I want to create in my project
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.yaml",
    "app.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index"
]

#Path function helps define the folder paths irrespective of the OS of the user (mac/windows/linus)
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) #path .split returns a tuple - (folder_name, file_name)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")