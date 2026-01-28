"""
Data Transformation Component
Handles feature engineering and preprocessing
"""
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

@dataclass
class DataTransformationConfig:
    """Configuration for data transformation"""
    preprocessor_obj_file_path: str = os.path.join('models', 'preprocessor.pkl')

class DataTransformation:
    """Handles data transformation and preprocessing"""
    
    def __init__(self):
        self.config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        """
        Create preprocessing pipeline
        
        Returns:
            ColumnTransformer: Preprocessing pipeline
        """
        try:
            # Define feature columns
            numeric_features = ['Age', 'Usage_Hours', 'Last_Maintenance_Days', 
                              'Technician_Experience']
            categorical_features = ['Maintenance_Type', 'Part_Replacement']
            
            # Create preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', StandardScaler(), numeric_features),
                    ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
                ])
            
            return preprocessor
            
        except Exception as e:
            print(f"Error creating transformer: {str(e)}")
            raise e
    
    def initiate_data_transformation(self, train_path, test_path):
        """
        Apply transformations to train and test data
        
        Args:
            train_path: Path to training data
            test_path: Path to test data
            
        Returns:
            tuple: Transformed train and test arrays, preprocessor object
        """
        try:
            print("Starting data transformation...")
            
            # Read train and test data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            print(f"Train data shape: {train_df.shape}")
            print(f"Test data shape: {test_df.shape}")
            
            # Get preprocessing object
            preprocessing_obj = self.get_data_transformer_object()
            
            # Define target column
            target_column_name = "Maintenance_Cost"
            drop_columns = [target_column_name, "Machine_ID"]
            
            # Separate features and target
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]
            
            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]
            
            print("Applying preprocessing...")
            
            # Fit and transform training data
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)
            
            # Combine features and target
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            
            # Save preprocessing object
            os.makedirs(os.path.dirname(self.config.preprocessor_obj_file_path), 
                       exist_ok=True)
            joblib.dump(preprocessing_obj, self.config.preprocessor_obj_file_path)
            
            print(f"Preprocessor saved to {self.config.preprocessor_obj_file_path}")
            print("Data transformation completed successfully")
            
            return (
                train_arr,
                test_arr,
                self.config.preprocessor_obj_file_path
            )
            
        except Exception as e:
            print(f"Error during data transformation: {str(e)}")
            raise e

if __name__ == "__main__":
    obj = DataTransformation()
    # Example usage - would need actual paths
    # obj.initiate_data_transformation('data/train.csv', 'data/test.csv')
