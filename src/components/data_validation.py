import sys
import os
from src.entity import DataValidationEntity
from src.custom_exception import CustomException
from src.logger import logging


class DataValiadtion:
    def __init__(self, config: DataValidationEntity):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        logging.info("Validating all file exists or not for training")
        try:
            validation_status = None

            all_files = os.listdir(
                os.path.join("artifacts", "data_ingestion", "samsum_dataset")
            )

            for file in all_files:
                if file not in self.config.required_folders:
                    validation_status = False
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.status_file, "w") as f:
                        f.write(f"Validation status: {validation_status}")
            logging.info("Validating all file exists or not for training - Completed")
            return validation_status

        except Exception as exp:
            raise CustomException(exp, sys)
