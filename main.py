from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=="__main__":
    try:
        triningpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(triningpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info(" Initiate the Data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(triningpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed")
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(triningpipelineconfig)
        logging.info("Initiate the Data Transformation")
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation completed")

        logging.info("Initiate the Model Trainer")
        model_trainer_config=ModelTrainerConfig(triningpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model Trainer completed")

        
    except Exception as e:
        raise NetworkSecurityException(e,sys) from e