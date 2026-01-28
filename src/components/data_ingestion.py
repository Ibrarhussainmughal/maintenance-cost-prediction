"""
Data Ingestion Component
Handles loading and initial processing of maintenance data
"""
import os
import sys
import pandas as pd
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    """Configuration for data ingestion"""
    raw_data_path: str = os.path.join('data', 'maintenance_data.csv')
    train_data_path: str = os.path.join('data', 'train.csv')
    test_data_path: str = os.path.join('data', 'test.csv')

class DataIngestion:
    """Handles data ingestion and initial split"""
    
    def __init__(self):
        self.config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        """
        Load data and perform train-test split
        
        Returns:
            tuple: Paths to train and test data
        """
        try:
            print("Starting data ingestion...")
            
            # Read the dataset
            df = pd.read_csv(self.config.raw_data_path)
            print(f"Loaded {len(df)} records from {self.config.raw_data_path}")
            
            # Create data directory if it doesn't exist
            os.makedirs(os.path.dirname(self.config.train_data_path), exist_ok=True)
            
            # Perform train-test split (80-20)
            from sklearn.model_selection import train_test_split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # Save train and test sets
            train_set.to_csv(self.config.train_data_path, index=False, header=True)
            test_set.to_csv(self.config.test_data_path, index=False, header=True)
            
            print(f"Train set: {len(train_set)} records")
            print(f"Test set: {len(test_set)} records")
            print("Data ingestion completed successfully")
            
            return (
                self.config.train_data_path,
                self.config.test_data_path
            )
            
        except Exception as e:
            print(f"Error during data ingestion: {str(e)}")
            raise e

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
