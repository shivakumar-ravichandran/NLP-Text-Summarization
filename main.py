import sys
from src.custom_exception import CustomException
from src.logger import logging
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "DATA INGESTION"
try:
    logging.info(f">>>>>> {STAGE_NAME} Stage Started <<<<<<")
    data_ingest_pipeline_obj = DataIngestionPipeline()
    data_ingest_pipeline_obj.execute_data_ingestion()
    logging.info(f">>>>>> {STAGE_NAME} Stage Completed <<<<<<")
except Exception as exp:
    raise CustomException(exp, sys)