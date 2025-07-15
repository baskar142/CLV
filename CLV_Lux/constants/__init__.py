import os
from datetime import date

DATABASE_NAME = "clv1"

COLLECTION_NAME = "clv_data"

MONGODB_URL_KEY = "MONGODB_URL"

PIPELINE_NAME: str = "CLV"
ARTIFACT_DIR: str = "artifact"

MODEL_FILE_NAME = "model.pkl"

FILE_NAME: str = "clv_data.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("config", "schema.yaml")


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "clv_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2