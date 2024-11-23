from dataclasses import dataclass
from pathlib import Path


@dataclass
class DataIngestionEntity:
    root_dir: Path
    source_url: str
    local_raw_folder: Path
    unzip_folder: Path
