from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """
    Configuration for data ingestion.

    Attributes:
        root_dir (Path): The root directory for data ingestion.
        source_dir (str): The source directory or URL for data retrieval.
        local_data_file (Path): The local file path for downloaded data.
        unzip_dir (Path): The directory where data will be extracted or stored after ingestion.
    """
    root_dir: Path
    source_dir: str
    local_data_file: Path
    unzip_dir: Path