from src.ChickenDisease.config.configuration import ConfigurationManager
from src.ChickenDisease.components.prepare_base_model import PrepareBaseModel
from src.ChickenDisease.logger import logging

STAGE_NAME = 'Prepare base model'

class PrepareBaseModelTrainingPipeline:
    def __init__(self,):
        pass


    def main(self):

        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            raise e
        

if __name__=='__main__':
    try:
        logging.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<<')
        obj= PrepareBaseModelTrainingPipeline()
        obj.main()
        logging.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x')
    except Exception as e:
        raise e