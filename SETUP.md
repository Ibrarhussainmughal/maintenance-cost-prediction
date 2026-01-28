# Project Setup and Environment Guide

This project uses a Conda environment to manage dependencies. Follow these instructions to set up and run the project locally.

## Prerequisite: Conda Environment
The project expects a Conda environment to be located in the `.conda/` folder within the project root.

### Running the Project
Since the project uses a local environment, you should use the Python executable directly from the `.conda` folder to ensure all dependencies (like Flask, Scikit-learn, and Pandas) are correctly loaded.

| Command | Action |
| :--- | :--- |
| `.\.conda\python.exe app.py` | **Start the Flask Web Server** |
| `.\.conda\python.exe train.py` | **Train the Machine Learning Model** |
| `.\.conda\python.exe generate_data.py` | **Generate Synthetic Maintenance Data** |
| `.\.conda\python.exe -m pip install <pkg>` | **Install a New Package** |

---

## Environment Verification

To verify you are using the correct environment, you can check your Python path and version:

### 1. Check Python Executable Path
Run the following command in your terminal:
```powershell
.\.conda\python.exe -c "import sys; print(sys.executable)"
```
**Expected Output:** Should contain `.../maintenance-cost-prediction/.conda/python.exe`

### 2. Check Python Version
```powershell
.\.conda\python.exe --version
```
**Expected Output:** `Python 3.11.14` (or similar version installed in your env)

---

## PowerShell Tips

### Create a Temporary Alias
To avoid typing the full path to the `.conda` executable, you can create a temporary alias for your current PowerShell session:

```powershell
Set-Alias -Name mypy "D:\projects\Maintenance-projects\maintenance-cost-prediction\.conda\python.exe"

# Now you can just run:
mypy app.py
```

---

## Dependency Management
All project dependencies are listed in `requirements.txt`. If you need to recreate the environment or install dependencies on a new machine:

1. Create a new environment: `conda create --prefix ./.conda python=3.11`
2. Activate it: `conda activate ./.conda`
3. Install dependencies: `pip install -r requirements.txt`
