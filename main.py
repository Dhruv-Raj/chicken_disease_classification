from src.ChickenDisease.logger import logging
from src.ChickenDisease.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.ChickenDisease.pipeline.stage_02_prepre_base_model import PrepareBaseModelTrainingPipeline



STAGE_NAME = 'Data Ingestion Stage'
try:
    logging.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    obj= DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x')
except Exception as e:
    raise e

STAGE_NAME= 'Prepare base model'
    
try:
    logging.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
    obj= PrepareBaseModelTrainingPipeline()
    obj.main()
    logging.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x')
except Exception as e:
    raise e