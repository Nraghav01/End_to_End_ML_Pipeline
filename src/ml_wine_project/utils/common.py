"""
In a modular MLOps folder structure, the utils folder (short for utilities) is used to store generic, reusable helper functions or scripts that are used across different parts of the project, such as logging, file handling, data processing, and configuration management. 
The main purposes of the utils folder are:
Modularity and Reusability: It centralizes common functionalities, avoiding code repetition across various modules (e.g., in data ingestion, model training, and evaluation components).
Separation of Concerns: It helps maintain a clean project structure by keeping low-level, generic tasks separate from the core business logic or specific ML pipeline steps.
Maintainability: By isolating these helper functions, updates or bug fixes to a utility can be made in a single location, which automatically applies the changes project-wide and reduces the risk of introducing errors in core modules.
Organization: It prevents the main folders (like src/components or src/pipelines) from becoming cluttered with miscellaneous functions that don't directly define the main workflow logic. 
Common contents of the utils folder in MLOps projects:
Logging and Exception Handling: Functions to set up standardized logging configurations and custom exception classes.
File I/O: Helper functions for reading from and writing to various file formats (e.g., .yaml, .json, .csv, .pkl), and handling file paths.
Data Handling: Small, generic data manipulation or formatting functions that aren't complex enough to warrant their own dedicated module.
Configuration Loading: Functions to parse and load configuration files, making the project configuration-driven.
Environment Setup: Scripts related to managing environment variables or dependencies. 
Ultimately, the utils folder acts as a toolbox of supporting functions that enhance productivity, consistency, and organization across the entire MLOps project lifecycle. . 

"""
import os
from box.exceptions import BoxValueError
import yaml
from ml_wine_project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

#@ensute_annotations - This is a decorater. Decorator to be used on functions with annotations. Runs type checks to enforce annotations. 
#                       Raises EnsureError if any argument passed to f is not of the type specified by the annotation. 
#                       Also raises EnsureError if the return value of f is not of the type specified by the annotation. Examples:
#ConfigBox - By default the a yaml file will be in dictionary format when loaded. This is used to convert the yaml dictionaryu in confix box type to call 
#           dict key as dict.key1 instead of only as dict['key1']. dict.key1 does not through error. Therefore, in the functions below, the output from yaml we convert
#           to config box

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"