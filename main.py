from src.ChickenDisease.logger import logging
from src.ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = 'Data Ingestion Stage'

if __name__=='__main__':
    try:
        logging.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
        obj= DataIngestionTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x')
    except Exception as e:
        raise e
    