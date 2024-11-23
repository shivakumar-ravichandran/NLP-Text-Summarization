import sys
from src.config.configuration_manager import ConfigurationManager
from src.entity import DataIngestionEntity
from src.components.data_ingestion import DataIngestion
from src.custom_exception import CustomException


class DataIngestionPipeline:
    def __init__(self):
        pass

    def execute_data_ingestion(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_ingestion_config: DataIngestionEntity = (
                config_manager_obj.data_ingestion_configuration()
            )
            data_ingestion_obj = DataIngestion(data_ingestion_config)
            is_file_download = data_ingestion_obj.download_source_file()
            if is_file_download:
                data_ingestion_obj.unzip_source_file()
        except Exception as exp:
            raise CustomException(exp, sys)
