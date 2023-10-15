from cnnClassifier import configure_logger 
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier.config.configuration import ConfigurationManager

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        self.logger = configure_logger("logs", "loggings.log")
    
    def main(self):
        try:
            self.logger.info(f"Stage: {STAGE_NAME} started")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            self.logger.info("Extracting data...")
            data_ingestion.extract_zip_file()
            self.logger.info(f"Stage: {STAGE_NAME} completed successfully.")
        except Exception as e:
            self.logger.error("Error in Data Ingestion Stage: %s", str(e))
            raise e

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()