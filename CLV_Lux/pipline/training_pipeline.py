import sys
from CLV_Lux.exception import CLVException
from CLV_Lux.logger import logging

from CLV_Lux.components.data_ingestion import DataIngestion
from CLV_Lux.entity.config_entity import DataIngestionConfig
from CLV_Lux.entity.artifact_entity import DataIngestionArtifact

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        Starts the data ingestion component
        """
        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from MongoDB")

            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Successfully got the train and test datasets from MongoDB")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")

            return data_ingestion_artifact

        except Exception as e:
            raise CLVException(e, sys) from e

    def run_pipeline(self) -> None:
        """
        Runs the entire pipeline
        """
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            # Next steps like data transformation, model training, etc. go here...

        except Exception as e:
            raise CLVException(e, sys) from e
