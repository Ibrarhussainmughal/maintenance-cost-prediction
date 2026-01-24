import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_model():
    """
    Trains the maintenance cost prediction model.
    Loads data, preprocesses features, trains a Random Forest Regressor,
    evaluates performance, and saves the model.
    """
    # Load data
    df = pd.read_csv('data/maintenance_data.csv')
    
    # Define features and target
    X = df.drop(['Machine_ID', 'Maintenance_Cost'], axis=1)
    y = df['Maintenance_Cost']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Preprocessing
    numeric_features = ['Age', 'Usage_Hours', 'Last_Maintenance_Days', 'Technician_Experience']
    categorical_features = ['Maintenance_Type', 'Part_Replacement']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numeric_features),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
        ])
    
    # Create pipeline
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])
    
    # Train model
    print("Training model...")
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Model Evaluation:")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"R2 Score: {r2:.4f}")
    
    # Save model
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/maintenance_model.joblib')
    print("Model saved to models/maintenance_model.joblib")

if __name__ == "__main__":
    train_model()
