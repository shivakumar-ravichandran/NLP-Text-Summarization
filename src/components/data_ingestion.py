import os
import sys
import urllib.request as request
from src.logger import logging
import zipfile
from src.custom_exception import CustomException
from src.entity import DataIngestionEntity


class DataIngestion:
    def __init__(self, config: DataIngestionEntity):
        self.config = config

    def download_source_file(self) -> bool:
        is_file_downloaded = False
        try:
            if not os.path.exists(self.config.local_raw_folder):
                filename, header = request.urlretrieve(
                    url=self.config.source_url, filename=self.config.local_raw_folder
                )
                logging.info("Source file downloaded into the system.")
                is_file_downloaded = True
            else:
                logging.info("Source File Already present in the system.")
            return is_file_downloaded
        except Exception as exp:
            raise CustomException(exp, sys)

    def unzip_source_file(self):
        try:
            os.makedirs(self.config.unzip_folder, exist_ok=True)
            with zipfile.ZipFile(self.config.local_raw_folder, "r") as zip_file:
                zip_file.extractall(self.config.unzip_folder)
            logging.info("Extracted all files into the system.")
        except Exception as exp:
            raise CustomException(exp, sys)
