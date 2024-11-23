from src.constants import *
from src.utils.common import CommonUtils
from box import ConfigBox
from src.custom_exception import CustomException
from src.entity import DataIngestionEntity
import sys


class ConfigurationManager:
    def __init__(self, config_path=CONFIG_FILE_PATH, params_path=PARAMS_FILE_PATH):
        self.config: ConfigBox = CommonUtils.read_yaml(config_path)
        self.params: ConfigBox = CommonUtils.read_yaml(params_path)

        CommonUtils.create_directories([self.config.artifacts_root])

    def DataIngestionConfiguration(self) -> DataIngestionEntity:
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
