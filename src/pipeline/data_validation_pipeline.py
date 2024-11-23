import sys
from src.config.configuration_manager import ConfigurationManager
from src.entity import DataValidationEntity
from src.components.data_validation import DataValiadtion
from src.custom_exception import CustomException


class DataValidationPipeline:
    def __init__(self):
        pass

    def execute_data_validation(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_validation_config: DataValidationEntity = (
                config_manager_obj.data_validation_configuration()
            )
            data_validation_obj = DataValiadtion(data_validation_config)
            data_validation_obj.validate_all_files_exist()
        except Exception as exp:
            raise CustomException(exp, sys)
