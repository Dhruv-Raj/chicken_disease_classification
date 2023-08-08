from src.ChickenDisease.config.configuration import ConfigurationManager
from src.ChickenDisease.components.data_ingestion import DataIngestion
from src.ChickenDisease.logger import logging

STAGE_NAME = 'Data Ingestion Stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        
if __name__=='__main__':
    try:
        logging.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x')
    except Exception as e:
        raise e