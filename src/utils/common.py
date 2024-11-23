import sys
import os
from pathlib import Path
from box import ConfigBox
from src.custom_exception import CustomException
import yaml
from ensure import ensure_annotations


class CommonUtils:

    @staticmethod
    @ensure_annotations
    def read_yaml(file_path: Path) -> ConfigBox:
        """Function to read the YAML file from the specified path

        Args:
            file_path (Path): file path

        Raises:
            CustomException: general exception

        Returns:
            ConfigBox: YAML content on config box format.`
        """
        try:
            with open(file=file_path, mode="r") as file:
                content = yaml.safe_load(file)
            return ConfigBox(content)
        except Exception as exp:
            raise CustomException(exp, sys)

    @staticmethod
    @ensure_annotations
    def create_directories(path_to_directories: list):
        """Function to create directories in the machine

        Args:
            path_to_directories (list): list of paths to be created

        Raises:
            CustomException: general exception
        """
        try:
            [os.makedirs(path, exist_ok=True) for path in path_to_directories]
        except Exception as exp:
            raise CustomException(exp, sys)
