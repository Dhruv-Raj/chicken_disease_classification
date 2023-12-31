from src.ChickenDisease.constants import *
from src.ChickenDisease.utils.main_utils import read_yaml, create_directories
from src.ChickenDisease.entity.config_entity import (DataIngestionConfig,  
                                                     PrepareBaseModelConfig,
                                                      PrepareCallbacksConfig,)
import os

# Creating Configuration Manager class

class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH):
        self.config= read_yaml(config_filepath)
        self.params= read_yaml(params_filepath)        
        create_directories([self.config.artifacts_root])
    
    # Creating Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config= self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config= DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL= config.source_URL,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir,
        )
        return data_ingestion_config    

    # Creating Base Model Configuration
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config 
    
    # Creating Callback Configuration
    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config.prepare_callbacks
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directories([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config.root_dir),
            tensorboard_root_log_dir=Path(config.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(config.checkpoint_model_filepath)
        )

        return prepare_callback_config
    
    # Creating 