import os
import sys
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.entity import DataTransformationEntity
from src.custom_exception import CustomException


class DataTransformation:
    def __init__(self, config: DataTransformationEntity):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        try:
            input_encoding = self.tokenizer(
                example_batch["dialogue"], max_length=1024, truncation=True
            )

            with self.tokenizer.as_target_tokenizer():
                target_encoding = self.tokenizer(
                    example_batch["summary"], max_length=128, truncation=True
                )

            return {
                "input_ids": input_encoding["input_ids"],
                "attention_mask": input_encoding["attention_mask"],
                "labels": target_encoding["input_ids"],
            }
        except Exception as exp:
            raise CustomException(exp, sys)

    def convert(self):
        samsum_dataset = load_from_disk(self.config.data_path)
        samsum_dataset_pt = samsum_dataset.map(
            self.convert_examples_to_features, batched=True
        )
        samsum_dataset_pt.save_to_disk(
            os.path.join(self.config.root_dir, "samsum_dataset")
        )
