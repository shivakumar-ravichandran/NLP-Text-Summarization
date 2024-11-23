import sys
from src.custom_exception import CustomException
from src.logger import logging
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.data_validation_pipeline import DataValidationPipeline
from src.pipeline.data_transformation import DataTransformationPipeline

STAGE_NAME = "DATA INGESTION"
try:
    logging.info(f">>>>>> {STAGE_NAME} Stage Started <<<<<<")
    data_ingest_pipeline_obj = DataIngestionPipeline()
    data_ingest_pipeline_obj.execute_data_ingestion()
    logging.info(f">>>>>> {STAGE_NAME} Stage Completed <<<<<<")
except Exception as exp:
    raise CustomException(exp, sys)


STAGE_NAME = "DATA VALIDATION"
try:
    logging.info(f">>>>>> {STAGE_NAME} Stage Started <<<<<<")
    data_ingest_pipeline_obj = DataValidationPipeline()
    data_ingest_pipeline_obj.execute_data_validation()
    logging.info(f">>>>>> {STAGE_NAME} Stage Completed <<<<<<")
except Exception as exp:
    raise CustomException(exp, sys)


STAGE_NAME = "DATA TRANSFORMATION"
try:
    logging.info(f">>>>>> {STAGE_NAME} Stage Started <<<<<<")
    data_ingest_pipeline_obj = DataTransformationPipeline()
    data_ingest_pipeline_obj.execute_data_transformation()
    logging.info(f">>>>>> {STAGE_NAME} Stage Completed <<<<<<")
except Exception as exp:
    raise CustomException(exp, sys)
