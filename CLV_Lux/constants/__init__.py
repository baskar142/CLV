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


TARGET_COLUMN = "CLV_Class"
PREPROCSSING_OBJECT_FILE_NAME = "preprocessing.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "clv_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2


"""
Data Validation realted contant start with DATA_VALIDATION VAR NAME
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"