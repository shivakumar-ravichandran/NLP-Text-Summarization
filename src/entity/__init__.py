from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionEntity:
    root_dir: Path
    source_url: str
    local_raw_folder: Path
    unzip_folder: Path


@dataclass
class DataValidationEntity:
    root_dir: Path
    status_file: Path
    required_folders: list
