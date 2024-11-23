from src.constants import *
from src.utils.common import CommonUtils
from box import ConfigBox
from src.custom_exception import CustomException
from src.entity import (
    DataIngestionEntity,
    DataValidationEntity,
    DataTransformationEntity,
)
import sys


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config: ConfigBox = CommonUtils.read_yaml(config_path)
        self.params: ConfigBox = CommonUtils.read_yaml(params_path)

        CommonUtils.create_directories([self.config.artifacts_root])

    def data_ingestion_configuration(self) -> DataIngestionEntity:
        try:
            data_ingestion_config = self.config.data_ingestion

            CommonUtils.create_directories([data_ingestion_config.root_dir])

            return DataIngestionEntity(
                root_dir=data_ingestion_config.root_dir,
                source_url=data_ingestion_config.source_url,
                local_raw_folder=data_ingestion_config.local_raw_folder,
                unzip_folder=data_ingestion_config.unzip_folder,
            )
        except Exception as exp:
            raise CustomException(exp, sys)

    def data_validation_configuration(self) -> DataValidationEntity:
        try:
            config = self.config.data_validation
            CommonUtils.create_directories([config.root_dir])
            return DataValidationEntity(
                root_dir=config.root_dir,
                status_file=config.status_file,
                required_folders=config.required_folders,
            )
        except Exception as exp:
            raise CustomException(exp, sys)

    def data_transformation_configuration(self) -> DataTransformationEntity:
        try:
            config = self.config.data_transformation
            CommonUtils.create_directories([config.root_dir])
            return DataTransformationEntity(
                root_dir=config.root_dir,
                data_path=config.data_path,
                tokenizer_name=config.tokenizer_name,
            )
        except Exception as exp:
            raise CustomException(exp, sys)
