import os
import zipfile
import gdown
from cnnClassifier.entity.config_entity import DataIngestionConfig
from cnnClassifier import configure_logger
from cnnClassifier.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize the DataIngestion instance.

        Args:
            config (DataIngestionConfig): Configuration for data ingestion.
        """
        self.config = config
        self.logger = configure_logger("logs", "loggings.log")

    def download_file(self) -> None:
        """
        Download data from a URL and save it to the local file.

        Raises:
            Exception: If an error occurs during the download.
        """
        try:
            dataset_url = self.config.source_dir
            zip_download_dir = self.config.local_data_file

            os.makedirs('artifacts/data_ingestion', exist_ok=True)

            self.logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_download_dir)

            self.logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            self.logger.error(f"Error during data download: {str(e)}")
            raise e

    def extract_zip_file(self) -> None:
        """
        Extract the contents of a ZIP file to a specified directory.

        Raises:
            Exception: If an error occurs during the extraction.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)