from cnnClassifier import configure_logger
from cnnClassifier.pipeline.data_ingestion_pipeline_001 import DataIngestionTrainingPipeline

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()