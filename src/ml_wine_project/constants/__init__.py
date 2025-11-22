#Here we are defining the paths of the confic, schema and params yanl files. 
#Naming this as constants as these paths will not change
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")