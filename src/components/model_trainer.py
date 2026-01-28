"""
Model Trainer Component
Handles model training and evaluation
"""
import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

@dataclass
class ModelTrainerConfig:
    """Configuration for model training"""
    trained_model_file_path: str = os.path.join('models', 'model.pkl')

class ModelTrainer:
    """Handles model training and evaluation"""
    
    def __init__(self):
        self.config = ModelTrainerConfig()
    
    def evaluate_models(self, X_train, y_train, X_test, y_test, models):
        """
        Evaluate multiple models
        
        Args:
            X_train: Training features
            y_train: Training target
            X_test: Test features
            y_test: Test target
            models: Dictionary of models to evaluate
            
        Returns:
            dict: Model performance scores
        """
        try:
            report = {}
            
            for model_name, model in models.items():
                print(f"\nTraining {model_name}...")
                
                # Train model
                model.fit(X_train, y_train)
                
                # Make predictions
                y_train_pred = model.predict(X_train)
                y_test_pred = model.predict(X_test)
                
                # Calculate metrics
                train_r2 = r2_score(y_train, y_train_pred)
                test_r2 = r2_score(y_test, y_test_pred)
                test_mae = mean_absolute_error(y_test, y_test_pred)
                test_rmse = np.sqrt(mean_squared_error(y_test, y_test_pred))
                
                report[model_name] = {
                    'train_r2': train_r2,
                    'test_r2': test_r2,
                    'test_mae': test_mae,
                    'test_rmse': test_rmse
                }
                
                print(f"{model_name} - Train R²: {train_r2:.4f}, Test R²: {test_r2:.4f}")
                print(f"{model_name} - MAE: {test_mae:.2f}, RMSE: {test_rmse:.2f}")
            
            return report
            
        except Exception as e:
            print(f"Error evaluating models: {str(e)}")
            raise e
    
    def initiate_model_trainer(self, train_array, test_array):
        """
        Train and evaluate models
        
        Args:
            train_array: Transformed training data
            test_array: Transformed test data
            
        Returns:
            float: Best model R² score
        """
        try:
            print("Starting model training...")
            
            # Split features and target
            X_train, y_train = train_array[:, :-1], train_array[:, -1]
            X_test, y_test = test_array[:, :-1], test_array[:, -1]
            
            # Define models to evaluate
            models = {
                "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
                "Gradient Boosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(random_state=42)
            }
            
            # Evaluate all models
            model_report = self.evaluate_models(X_train, y_train, X_test, y_test, models)
            
            # Get best model based on test R² score
            best_model_name = max(model_report, key=lambda x: model_report[x]['test_r2'])
            best_model_score = model_report[best_model_name]['test_r2']
            best_model = models[best_model_name]
            
            print(f"\n{'='*50}")
            print(f"Best Model: {best_model_name}")
            print(f"Test R² Score: {best_model_score:.4f}")
            print(f"{'='*50}")
            
            if best_model_score < 0.6:
                print("Warning: Best model has R² score < 0.6")
            
            # Save the best model
            os.makedirs(os.path.dirname(self.config.trained_model_file_path), 
                       exist_ok=True)
            joblib.dump(best_model, self.config.trained_model_file_path)
            
            print(f"Best model saved to {self.config.trained_model_file_path}")
            
            return best_model_score
            
        except Exception as e:
            print(f"Error during model training: {str(e)}")
            raise e

if __name__ == "__main__":
    # Example usage
    pass
