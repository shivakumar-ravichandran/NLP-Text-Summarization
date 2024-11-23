import sys
from src.config.configuration_manager import ConfigurationManager
from src.entity import DataTransformationEntity
from src.components.data_transformation import DataTransformation
from src.custom_exception import CustomException


class DataTransformationPipeline:
    def __init__(self):
        pass

    def execute_data_transformation(self):
        try:
            config_manager_obj = ConfigurationManager()
            data_transformation_conf: DataTransformationEntity = (
                config_manager_obj.data_transformation_configuration()
            )
            data_transformation_obj = DataTransformation(data_transformation_conf)
            data_transformation_obj.convert()
        except Exception as exp:
            raise CustomException(exp, sys)
