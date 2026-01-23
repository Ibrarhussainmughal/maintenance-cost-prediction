from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the model
model = joblib.load('models/maintenance_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        data = {
            'Age': [float(request.form['age'])],
            'Usage_Hours': [float(request.form['usage_hours'])],
            'Maintenance_Type': [request.form['maintenance_type']],
            'Last_Maintenance_Days': [int(request.form['last_maintenance_days'])],
            'Part_Replacement': [int(request.form['part_replacement'])],
            'Technician_Experience': [float(request.form['technician_experience'])]
        }
        
        # Create DataFrame
        df_input = pd.DataFrame(data)
        
        # Predict
        prediction = model.predict(df_input)[0]
        
        return render_template('index.html', 
                               prediction_text=f'Estimated Maintenance Cost: ${prediction:.2f}',
                               form_data=request.form)
    except Exception as e:
        return render_template('index.html', error_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
