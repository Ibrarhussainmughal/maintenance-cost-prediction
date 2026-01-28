"""
Configuration settings for the maintenance cost prediction project
"""
import os
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'maintenance_data.csv')
TRAIN_DATA_PATH = os.path.join(DATA_DIR, 'train.csv')
TEST_DATA_PATH = os.path.join(DATA_DIR, 'test.csv')

# Model paths
MODEL_DIR = os.path.join(BASE_DIR, 'models')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')
PREPROCESSOR_PATH = os.path.join(MODEL_DIR, 'preprocessor.pkl')

# Feature configuration
NUMERIC_FEATURES = ['Age', 'Usage_Hours', 'Last_Maintenance_Days', 'Technician_Experience']
CATEGORICAL_FEATURES = ['Maintenance_Type', 'Part_Replacement']
TARGET_COLUMN = 'Maintenance_Cost'
ID_COLUMN = 'Machine_ID'

# Model configuration
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 100

# Maintenance type options
MAINTENANCE_TYPES = ['Routine', 'Preventive', 'Corrective']

# Flask configuration
FLASK_HOST = '0.0.0.0'
FLASK_PORT = 5000
FLASK_DEBUG = True

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
