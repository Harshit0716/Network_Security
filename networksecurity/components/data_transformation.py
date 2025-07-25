import sys
import os
import numpy as np
import pandas as pd
from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

from networksecurity.constants.training_pipeline import TARGET_COLUMN
from networksecurity.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import(
    DataTransformationArtifact,
    DataValidationArtifact
)
from networksecurity.utils.main_utils.utils import save_numpy_array_data, save_object



class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact,
                 data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact: DataValidationArtifact = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        """
        Read data from a CSV file and return as a DataFrame.
        """
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def get_data_transformer_object(cls)-> Pipeline:
        """
        Create a data transformation pipeline with KNN Imputer.
        """
        logging.info("Entered the get_data_transformer_object method of DataTransformation class")
        try:
            imputer: KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info(f"Initialize KNNImputer with: {DATA_TRANSFORMATION_IMPUTER_PARAMS}")
            pipeline: Pipeline = Pipeline([
                ('imputer', imputer)
            ])
            return pipeline
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e


    def initiate_data_transformation(self) -> DataTransformationArtifact:
        """
        Initiates the data transformation process.
        """
        logging.info("Entered the initiate_data_transformation method of DataTransformation class")
        try:
            logging.info("Starting data transformation")
            # Read the input data
            train_df=DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df=DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            #training dataframe
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)

            #testing dataframe
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)

            preprocessor = self.get_data_transformer_object()
            preprocessor_object=preprocessor.fit(input_feature_train_df)
            transformed_input_feature_train = preprocessor_object.transform(input_feature_train_df)
            transformed_input_feature_test = preprocessor_object.transform(input_feature_test_df)
            train_arr = np.c_[transformed_input_feature_train, np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_feature_test, np.array(target_feature_test_df)]

            ## Save numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr,)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr,)
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object,)

            ##preparing artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact

        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
