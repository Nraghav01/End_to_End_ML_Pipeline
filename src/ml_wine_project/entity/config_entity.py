import os

#Defining Data IUngestion entity as per workflow in readme
from dataclasses import dataclass
from pathlib import Path

#We are defining an ingestion class here
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


