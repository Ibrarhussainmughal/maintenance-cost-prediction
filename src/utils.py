"""
Utility functions for the maintenance cost prediction project
"""
import os
import sys
import joblib
import pandas as pd
import numpy as np
from typing import Any, Dict, List, Tuple

def save_object(file_path: str, obj: Any) -> None:
    """
    Save a Python object to a file using joblib
    
    Args:
        file_path: Path where object should be saved
        obj: Object to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            joblib.dump(obj, file_obj)
            
    except Exception as e:
        raise Exception(f"Error saving object: {str(e)}")

def load_object(file_path: str) -> Any:
    """
    Load a Python object from a file using joblib
    
    Args:
        file_path: Path to the saved object
        
    Returns:
        Loaded object
    """
    try:
        with open(file_path, "rb") as file_obj:
            return joblib.load(file_obj)
            
    except Exception as e:
        raise Exception(f"Error loading object: {str(e)}")

def evaluate_model(X_train: np.ndarray, y_train: np.ndarray,
                   X_test: np.ndarray, y_test: np.ndarray,
                   models: Dict[str, Any]) -> Dict[str, float]:
    """
    Evaluate multiple models and return their scores
    
    Args:
        X_train: Training features
        y_train: Training target
        X_test: Test features
        y_test: Test target
        models: Dictionary of models to evaluate
        
    Returns:
        Dictionary of model names and their R² scores
    """
    try:
        from sklearn.metrics import r2_score
        
        report = {}
        
        for model_name, model in models.items():
            # Train model
            model.fit(X_train, y_train)
            
            # Predict
            y_test_pred = model.predict(X_test)
            
            # Get R² score
            test_model_score = r2_score(y_test, y_test_pred)
            
            report[model_name] = test_model_score
            
        return report
        
    except Exception as e:
        raise Exception(f"Error evaluating models: {str(e)}")

def get_feature_names(preprocessor, numeric_features: List[str], 
                      categorical_features: List[str]) -> List[str]:
    """
    Get feature names after preprocessing
    
    Args:
        preprocessor: Fitted ColumnTransformer
        numeric_features: List of numeric feature names
        categorical_features: List of categorical feature names
        
    Returns:
        List of all feature names after transformation
    """
    try:
        # Get categorical feature names after one-hot encoding
        cat_encoder = preprocessor.named_transformers_['cat']
        cat_feature_names = cat_encoder.get_feature_names_out(categorical_features)
        
        # Combine numeric and categorical feature names
        feature_names = numeric_features + list(cat_feature_names)
        
        return feature_names
        
    except Exception as e:
        raise Exception(f"Error getting feature names: {str(e)}")

def create_sample_data() -> pd.DataFrame:
    """
    Create a sample dataframe for testing
    
    Returns:
        Sample DataFrame with correct schema
    """
    sample_data = {
        'Age': [5.0],
        'Usage_Hours': [5000.0],
        'Maintenance_Type': ['Routine'],
        'Last_Maintenance_Days': [100],
        'Part_Replacement': [0],
        'Technician_Experience': [10.0]
    }
    
    return pd.DataFrame(sample_data)

def validate_input_data(df: pd.DataFrame) -> Tuple[bool, str]:
    """
    Validate input data for predictions
    
    Args:
        df: Input DataFrame
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    required_columns = ['Age', 'Usage_Hours', 'Maintenance_Type', 
                       'Last_Maintenance_Days', 'Part_Replacement', 
                       'Technician_Experience']
    
    # Check if all required columns are present
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        return False, f"Missing columns: {missing_columns}"
    
    # Check data types and ranges
    try:
        if df['Age'].iloc[0] < 0 or df['Age'].iloc[0] > 50:
            return False, "Age must be between 0 and 50 years"
        
        if df['Usage_Hours'].iloc[0] < 0:
            return False, "Usage hours must be positive"
        
        if df['Maintenance_Type'].iloc[0] not in ['Routine', 'Preventive', 'Corrective']:
            return False, "Maintenance type must be Routine, Preventive, or Corrective"
        
        if df['Last_Maintenance_Days'].iloc[0] < 0 or df['Last_Maintenance_Days'].iloc[0] > 365:
            return False, "Last maintenance days must be between 0 and 365"
        
        if df['Part_Replacement'].iloc[0] not in [0, 1]:
            return False, "Part replacement must be 0 or 1"
        
        if df['Technician_Experience'].iloc[0] < 0 or df['Technician_Experience'].iloc[0] > 50:
            return False, "Technician experience must be between 0 and 50 years"
        
        return True, ""
        
    except Exception as e:
        return False, f"Validation error: {str(e)}"
