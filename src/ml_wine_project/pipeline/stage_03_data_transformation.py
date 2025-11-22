from ml_wine_project.config.configuration import ConfigurationManager
from ml_wine_project.components.data_transformation import DataTransformation
from ml_wine_project import logger
from pathlib import Path


#For this pipeline, we will execute stage 03 only when the status.txt from the validation pipeline stage 02 is TRUE

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                #Checking for true status of validation pipeline
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)