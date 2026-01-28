# Quick Start Guide

## Maintenance Cost Prediction - Getting Started in 5 Minutes

### Prerequisites
- Python 3.8 or higher installed
- pip package manager
- Git (optional, for cloning)

---

## Step 1: Setup Environment (2 minutes)

### Clone or Download the Project
```bash
# If using Git
git clone <repository-url>
cd maintenance-cost-prediction

# Or download and extract the ZIP file
```

### Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Step 2: Generate Data (30 seconds)

```bash
python generate_data.py
```

**Expected Output:**
```
Generated 2000 samples and saved to data/maintenance_data.csv
```

**What this does:**
- Creates synthetic maintenance data
- Generates 2,000 realistic records
- Saves to `data/maintenance_data.csv`

---

## Step 3: Train the Model (1 minute)

### Option A: Using Modular Pipeline (Recommended)
```bash
python -m src.pipeline.train_pipeline
```

### Option B: Using Legacy Script
```bash
python train.py
```

**Expected Output:**
```
============================================================
STARTING TRAINING PIPELINE
============================================================

[STEP 1/3] Data Ingestion
------------------------------------------------------------
Loaded 2000 records from data/maintenance_data.csv
Train set: 1600 records
Test set: 400 records

[STEP 2/3] Data Transformation
------------------------------------------------------------
Train data shape: (1600, 8)
Test data shape: (400, 8)
Applying preprocessing...
Preprocessor saved to models/preprocessor.pkl

[STEP 3/3] Model Training
------------------------------------------------------------
Training Random Forest...
Training Gradient Boosting...
Training Linear Regression...
Training Decision Tree...

==================================================
Best Model: Random Forest
Test R² Score: 0.9500
==================================================

============================================================
TRAINING PIPELINE COMPLETED SUCCESSFULLY
Final Model R² Score: 0.9500
============================================================
```

**What this does:**
- Splits data into train/test sets
- Preprocesses features
- Trains multiple ML models
- Selects best performing model
- Saves model to `models/model.pkl`

---

## Step 4: Run Web Application (30 seconds)

```bash
python app.py
```

**Expected Output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

### Access the Application
1. Open your browser
2. Go to: `http://127.0.0.1:5000`
3. Fill in the form with machine details
4. Click "Predict Cost"
5. See the predicted maintenance cost!

---

## Step 5: Explore the Analysis (Optional)

```bash
jupyter notebook notebooks/maintenance_analysis.ipynb
```

**What you'll find:**
- Exploratory Data Analysis (EDA)
- Data visualizations
- Feature correlations
- Model insights

---

## Quick Test - Make a Prediction

### Using Python
```python
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# Create sample data
data = CustomData(
    age=5.0,
    usage_hours=5000.0,
    maintenance_type="Routine",
    last_maintenance_days=100,
    part_replacement=0,
    technician_experience=10.0
)

# Get prediction
pipeline = PredictPipeline()
df = data.get_data_as_dataframe()
result = pipeline.predict(df)

print(f"Predicted Maintenance Cost: ${result[0]:.2f}")
```

### Using Web Interface
1. Navigate to `http://127.0.0.1:5000`
2. Enter values:
   - Machine Age: 5 years
   - Usage Hours: 5000
   - Maintenance Type: Routine
   - Days Since Last Maintenance: 100
   - Part Replacement: No
   - Technician Experience: 10 years
3. Click "Predict Cost"
4. View result!

---

## Troubleshooting

### Issue: Module not found
**Solution:** Make sure you're in the project directory and virtual environment is activated
```bash
pip install -r requirements.txt
```

### Issue: Data file not found
**Solution:** Run the data generation script first
```bash
python generate_data.py
```

### Issue: Model file not found
**Solution:** Train the model first
```bash
python -m src.pipeline.train_pipeline
```

### Issue: Port 5000 already in use
**Solution:** Change port in app.py or kill the process using port 5000
```python
# In app.py, change:
app.run(host='0.0.0.0', port=5001, debug=True)
```

---

## Project Structure Quick Reference

```
maintenance-cost-prediction/
├── data/                    # Generated data files
├── models/                  # Trained models
├── notebooks/               # Jupyter notebooks
├── src/                     # Source code
│   ├── components/         # ML components
│   └── pipeline/           # Training & prediction pipelines
├── templates/              # Web UI templates
├── app.py                  # Flask application
├── generate_data.py        # Data generator
└── requirements.txt        # Dependencies
```

---

## Next Steps

1. **Explore the Code**
   - Check out `src/components/` for ML components
   - Review `src/pipeline/` for orchestration
   - Examine `app.py` for web application

2. **Modify and Experiment**
   - Change model parameters in `src/components/model_trainer.py`
   - Add new features in `generate_data.py`
   - Customize UI in `templates/index.html`

3. **Extend the Project**
   - Add unit tests
   - Implement hyperparameter tuning
   - Create a REST API
   - Deploy to cloud

---

## Common Commands

```bash
# Generate data
python generate_data.py

# Train model (modular)
python -m src.pipeline.train_pipeline

# Train model (legacy)
python train.py

# Run web app
python app.py

# Run Jupyter notebook
jupyter notebook

# Install package in development mode
pip install -e .

# Format code
black src/

# Lint code
flake8 src/
```

---

## Support

- **Documentation**: See README.md
- **Issues**: Open an issue on GitHub
- **Questions**: Contact the author

---

**Estimated Total Time**: 5 minutes
**Difficulty**: Beginner-friendly
**Status**: ✅ Ready to run!

Happy predicting! 🚀
