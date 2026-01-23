# Maintenance Cost Prediction (End-to-End ML Project)

This project implements an end-to-end Machine Learning pipeline to predict the maintenance cost of industrial machines. It includes synthetic data generation, model training using a Random Forest Regressor, and a simple Flask web application for deployment.

## Project Structure

\`\`\`
maintenance_cost_prediction/
├── data/
│   └── maintenance_data.csv      # Synthetic dataset
├── models/
│   └── maintenance_model.joblib  # Trained ML model
├── templates/
│   └── index.html                # Web application frontend
├── app.py                        # Flask web application
├── generate_data.py              # Script to generate synthetic data
├── train.py                      # Script to train the ML model
└── requirements.txt              # Python dependencies
\`\`\`

## Setup and Installation

1.  **Clone the repository:**
    \`\`\`bash
    git clone <repository-url>
    cd maintenance_cost_prediction
    \`\`\`

2.  **Install dependencies:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

## Usage

### 1. Generate Data

Run the script to create the synthetic dataset in the \`data/\` directory.

\`\`\`bash
python generate_data.py
\`\`\`

### 2. Train Model

Run the training script. This will perform data preprocessing, train a Random Forest Regressor, evaluate its performance, and save the trained model to \`models/maintenance_model.joblib\`.

\`\`\`bash
python train.py
\`\`\`

### 3. Run Web Application

Start the Flask application.

\`\`\`bash
python app.py
\`\`\`

The application will be available at \`http://127.0.0.1:5000\`. You can use the web interface to input machine parameters and get a real-time maintenance cost prediction.

## Model Details

The model is a **Random Forest Regressor** trained on the following features:

| Feature | Type | Description |
| :--- | :--- | :--- |
| **Age** | Numerical | Age of the machine in years. |
| **Usage\_Hours** | Numerical | Total operational hours of the machine. |
| **Maintenance\_Type** | Categorical | Type of maintenance (Routine, Preventive, Corrective). |
| **Last\_Maintenance\_Days** | Numerical | Days elapsed since the last maintenance. |
| **Part\_Replacement** | Binary | Whether a major part replacement was involved (0=No, 1=Yes). |
| **Technician\_Experience** | Numerical | Experience of the technician in years. |

The target variable is **Maintenance\_Cost** (in USD).
