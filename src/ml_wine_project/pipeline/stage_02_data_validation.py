#Now we create the stage 2 data validation pipeline here
from ml_wine_project.config.configuration import ConfigurationManager
from ml_wine_project.components.data_validation import DataValiadtion
from ml_wine_project import logger


STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()