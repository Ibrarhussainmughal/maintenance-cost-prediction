import pandas as pd
import numpy as np
import os

def generate_maintenance_data(n_samples=1000):
    np.random.seed(42)
    
    # Features
    machine_ids = [f"M_{i:04d}" for i in range(n_samples)]
    age = np.random.uniform(1, 15, n_samples)  # 1 to 15 years
    usage_hours = age * np.random.uniform(1000, 2500, n_samples)
    maintenance_type = np.random.choice(['Routine', 'Preventive', 'Corrective'], n_samples, p=[0.5, 0.3, 0.2])
    last_maintenance_days = np.random.randint(10, 365, n_samples)
    part_replacement = np.random.choice([0, 1], n_samples, p=[0.7, 0.3])
    technician_experience = np.random.uniform(1, 20, n_samples)
    
    # Base cost
    base_cost = 200
    
    # Cost calculation logic
    cost = (
        base_cost +
        (age * 50) +
        (usage_hours * 0.05) +
        (last_maintenance_days * 0.2) +
        (part_replacement * 500) -
        (technician_experience * 5) +
        np.random.normal(0, 50, n_samples) # Noise
    )
    
    # Adjust cost based on maintenance type
    type_multipliers = {'Routine': 1.0, 'Preventive': 1.5, 'Corrective': 2.5}
    cost = cost * np.array([type_multipliers[t] for t in maintenance_type])
    
    df = pd.DataFrame({
        'Machine_ID': machine_ids,
        'Age': age,
        'Usage_Hours': usage_hours,
        'Maintenance_Type': maintenance_type,
        'Last_Maintenance_Days': last_maintenance_days,
        'Part_Replacement': part_replacement,
        'Technician_Experience': technician_experience,
        'Maintenance_Cost': cost
    })
    
    # Ensure no negative costs
    df['Maintenance_Cost'] = df['Maintenance_Cost'].clip(lower=100)
    
    return df

if __name__ == "__main__":
    data = generate_maintenance_data(2000)
    os.makedirs('data', exist_ok=True)
    data.to_csv('data/maintenance_data.csv', index=False)
    print(f"Generated 2000 samples and saved to data/maintenance_data.csv")
