import os
from TextSummarizer.logging import logger
from TextSummarizer.entity import DataValidationConfig

class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config


    
    def validate_all_files_exist(self):
        try:
            validation_status = None

            all_files = os.listdir(self.config.data_path)

            required_files = set(self.config.ALL_REQUIRED_FILES)
            available_files = set(all_files)

            validation_status = required_files.issubset(available_files)

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        
        except Exception as e:
            raise e