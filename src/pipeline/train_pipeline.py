"""
Training Pipeline
Orchestrates the complete training workflow
"""
import os
import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

class TrainPipeline:
    """Complete training pipeline"""
    
    def __init__(self):
        pass
    
    def run_pipeline(self):
        """
        Execute the complete training pipeline
        
        Returns:
            float: Model performance score
        """
        try:
            print("="*60)
            print("STARTING TRAINING PIPELINE")
            print("="*60)
            
            # Step 1: Data Ingestion
            print("\n[STEP 1/3] Data Ingestion")
            print("-"*60)
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            
            # Step 2: Data Transformation
            print("\n[STEP 2/3] Data Transformation")
            print("-"*60)
            data_transformation = DataTransformation()
            train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
                train_data_path, test_data_path
            )
            
            # Step 3: Model Training
            print("\n[STEP 3/3] Model Training")
            print("-"*60)
            model_trainer = ModelTrainer()
            score = model_trainer.initiate_model_trainer(train_arr, test_arr)
            
            print("\n" + "="*60)
            print("TRAINING PIPELINE COMPLETED SUCCESSFULLY")
            print(f"Final Model R² Score: {score:.4f}")
            print("="*60)
            
            return score
            
        except Exception as e:
            print(f"\nERROR IN TRAINING PIPELINE: {str(e)}")
            raise e

if __name__ == "__main__":
    pipeline = TrainPipeline()
    pipeline.run_pipeline()
