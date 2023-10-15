from pathlib import Path
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier.constants import *
from cnnClassifier.utils.common import  *

class ConfigurationManager:
    def __init__(self, 
                config_filepath: Path = None, 
                params_filepath: Path = None):
        """
        Initialize the ConfigurationManager.

        Args:
            config_filepath (Path, optional): The path to the configuration file.
            params_filepath (Path, optional): The path to the parameters file.
        """
        if config_filepath is None:
            config_filepath = CONFIG_FILE_PATH

        if params_filepath is None:
            params_filepath = PARAMS_FILE_PATH

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        # Create directories if needed
        create_directories([self.config.artifact_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Get the data ingestion configuration.

        Returns:
            DataIngestionConfig: The data ingestion configuration.
        """
        config = self.config.data_ingestion

        # Create directories if needed
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_dir=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
