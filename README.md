# Maintenance Cost Prediction - End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.0-green)
![scikit--learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🎯 Project Overview

An end-to-end machine learning solution for predicting maintenance costs of industrial machines. This project demonstrates a complete ML workflow from data generation to model deployment with a user-friendly web interface.

### 🌟 Key Features

- **Modular Architecture**: Clean separation of concerns with dedicated components
- **Multiple ML Models**: Comparison of Random Forest, Gradient Boosting, Linear Regression, and Decision Tree
- **Production-Ready Pipeline**: Automated training and prediction pipelines
- **Web Application**: Interactive Flask-based UI for real-time predictions
- **Comprehensive Analysis**: Jupyter notebook with detailed EDA and insights

## 📊 Project Structure

```
maintenance-cost-prediction/
│
├── data/                          # Data directory (gitignored)
│   ├── maintenance_data.csv       # Generated dataset
│   ├── train.csv                  # Training data
│   └── test.csv                   # Test data
│
├── models/                        # Saved models (gitignored)
│   ├── model.pkl                  # Best trained model
│   └── preprocessor.pkl           # Data preprocessor
│
├── notebooks/                     # Jupyter notebooks
│   └── maintenance_analysis.ipynb # EDA and analysis
│
├── src/                          # Source code
│   ├── components/               # ML components
│   │   ├── data_ingestion.py    # Data loading and splitting
│   │   ├── data_transformation.py # Feature engineering
│   │   └── model_trainer.py     # Model training and evaluation
│   │
│   └── pipeline/                # ML pipelines
│       ├── train_pipeline.py    # Training orchestration
│       └── predict_pipeline.py  # Prediction pipeline
│
├── templates/                    # Flask templates
│   └── index.html               # Web UI
│
├── app.py                       # Flask application
├── generate_data.py             # Synthetic data generator
├── train.py                     # Legacy training script
├── setup.py                     # Package setup
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd maintenance-cost-prediction
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### 1. Generate Synthetic Data
```bash
python generate_data.py
```
This creates a dataset of 2,000 maintenance records with realistic patterns.

#### 2. Train the Model

**Option A: Using the modular pipeline (Recommended)**
```bash
python -m src.pipeline.train_pipeline
```

**Option B: Using the legacy script**
```bash
python train.py
```

#### 3. Run the Web Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your browser to use the prediction interface.

#### 4. Explore the Analysis
Open `notebooks/maintenance_analysis.ipynb` in Jupyter to see detailed exploratory data analysis.

## 📈 Model Features

### Input Features

| Feature | Type | Description |
|---------|------|-------------|
| **Age** | Numerical | Machine age in years (1-15) |
| **Usage Hours** | Numerical | Total operational hours |
| **Maintenance Type** | Categorical | Routine, Preventive, or Corrective |
| **Last Maintenance Days** | Numerical | Days since last maintenance (10-365) |
| **Part Replacement** | Binary | Major part replacement (0=No, 1=Yes) |
| **Technician Experience** | Numerical | Technician experience in years (1-20) |

### Target Variable

- **Maintenance Cost**: Predicted cost in USD

### Model Performance

The system evaluates multiple algorithms and selects the best performer:
- Random Forest Regressor (Primary)
- Gradient Boosting Regressor
- Linear Regression
- Decision Tree Regressor

Expected performance metrics:
- **R² Score**: ~0.95+
- **MAE**: ~$50-100
- **RMSE**: ~$75-150

## 🔧 Technical Details

### Data Generation

The synthetic dataset simulates realistic maintenance scenarios:
- Base cost calculation with multiple factors
- Maintenance type multipliers (Routine: 1.0x, Preventive: 1.5x, Corrective: 2.5x)
- Random noise to simulate real-world variability
- Ensures no negative costs

### Preprocessing Pipeline

1. **Numerical Features**: StandardScaler normalization
2. **Categorical Features**: OneHotEncoder encoding
3. **Pipeline Integration**: Sklearn ColumnTransformer

### Model Training

- Train/Test split: 80/20
- Cross-validation ready
- Hyperparameter optimization capable
- Model persistence with joblib

## 🌐 Web Application

The Flask application provides:
- Clean, responsive UI
- Real-time predictions
- Input validation
- Error handling
- Form data persistence

### API Endpoints

- `GET /`: Home page with prediction form
- `POST /predict`: Submit prediction request

## 📊 Analysis Insights

Key findings from the exploratory analysis:

1. **Cost Distribution**: Most maintenance costs are predictable with few outliers
2. **Age Impact**: Older machines generally require higher maintenance costs
3. **Maintenance Type**: Corrective maintenance is significantly more expensive
4. **Usage Hours**: Strong correlation with maintenance costs
5. **Part Replacement**: Major cost driver when required

## 🛠️ Development

### Running Tests
```bash
pytest tests/
```

### Code Formatting
```bash
black src/
```

### Linting
```bash
flake8 src/
```

## 📝 Future Enhancements

- [ ] Add more sophisticated feature engineering
- [ ] Implement hyperparameter tuning (GridSearchCV/RandomizedSearchCV)
- [ ] Add model monitoring and drift detection
- [ ] Create REST API with FastAPI
- [ ] Add Docker containerization
- [ ] Implement CI/CD pipeline
- [ ] Add more visualization in web UI
- [ ] Create model explainability dashboard (SHAP values)
- [ ] Add database integration for production data
- [ ] Implement user authentication

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Ibrar Hussain Mughal**
- GitHub: [@Ibrarhussainmughal](https://github.com/Ibrarhussainmughal)
- Email: ibrar.ali69.ia@gmail.com

## 🙏 Acknowledgments

- Scikit-learn for the excellent ML library
- Flask for the web framework
- The open-source community

## 📞 Contact

For questions or feedback, please open an issue or contact the author directly.

---

**Note**: This is a demonstration project using synthetic data. For production use, replace with real maintenance data and perform thorough validation.
