"""
Prediction Pipeline
Handles predictions for new data
"""
import os
import sys
import pandas as pd
import joblib

class PredictPipeline:
    """Prediction pipeline for new data"""
    
    def __init__(self):
        self.model_path = os.path.join('models', 'model.pkl')
        self.preprocessor_path = os.path.join('models', 'preprocessor.pkl')
    
    def predict(self, features):
        """
        Make predictions on new data
        
        Args:
            features: DataFrame with input features
            
        Returns:
            array: Predictions
        """
        try:
            # Load model and preprocessor
            model = joblib.load(self.model_path)
            preprocessor = joblib.load(self.preprocessor_path)
            
            # Transform features
            data_scaled = preprocessor.transform(features)
            
            # Make predictions
            predictions = model.predict(data_scaled)
            
            return predictions
            
        except Exception as e:
            print(f"Error during prediction: {str(e)}")
            raise e

class CustomData:
    """Custom data class for creating prediction inputs"""
    
    def __init__(self,
                 age: float,
                 usage_hours: float,
                 maintenance_type: str,
                 last_maintenance_days: int,
                 part_replacement: int,
                 technician_experience: float):
        
        self.age = age
        self.usage_hours = usage_hours
        self.maintenance_type = maintenance_type
        self.last_maintenance_days = last_maintenance_days
        self.part_replacement = part_replacement
        self.technician_experience = technician_experience
    
    def get_data_as_dataframe(self):
        """
        Convert custom data to DataFrame
        
        Returns:
            DataFrame: Input data in correct format
        """
        try:
            custom_data_input_dict = {
                "Age": [self.age],
                "Usage_Hours": [self.usage_hours],
                "Maintenance_Type": [self.maintenance_type],
                "Last_Maintenance_Days": [self.last_maintenance_days],
                "Part_Replacement": [self.part_replacement],
                "Technician_Experience": [self.technician_experience]
            }
            
            return pd.DataFrame(custom_data_input_dict)
            
        except Exception as e:
            print(f"Error creating dataframe: {str(e)}")
            raise e

if __name__ == "__main__":
    # Example usage
    custom_data = CustomData(
        age=5.0,
        usage_hours=5000.0,
        maintenance_type="Routine",
        last_maintenance_days=100,
        part_replacement=0,
        technician_experience=10.0
    )
    
    pred_df = custom_data.get_data_as_dataframe()
    print("Input DataFrame:")
    print(pred_df)
    
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    print(f"\nPredicted Maintenance Cost: ${results[0]:.2f}")
