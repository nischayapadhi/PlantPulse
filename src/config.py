"""
config.py
Configuration file for PlantPulse project.
Stores directory paths, file names, and dataset schema constants to ensure consistency
across all notebooks and source scripts.
"""

from pathlib import Path

# ---------------------------------------------------------
# Path Management
# ---------------------------------------------------------
# Dynamically locate the project root regardless of where scripts are run
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Data directories based on our locked structure
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "01_raw"
INTERIM_DATA_DIR = DATA_DIR / "02_interim"
PROCESSED_DATA_DIR = DATA_DIR / "03_processed"

# I/O Files
RAW_DATA_FILE = RAW_DATA_DIR / "ai4i2020.csv"
PROCESSED_DATA_FILE = PROCESSED_DATA_DIR / "plantpulse_processed.csv"


# ---------------------------------------------------------
# Dataset Schema Constants
# ---------------------------------------------------------
# Identifiers and Categorical
ID_COLS = ["UDI", "Product ID"]
CAT_COLS = ["Type"] # L, M, H (Low, Medium, High quality)

# Continuous Sensor Features
NUMERIC_FEATURES = [
    "Air temperature [K]",
    "Process temperature [K]",
    "Rotational speed [rpm]",
    "Torque [Nm]",
    "Tool wear [min]"
]

# Engineered Features (To be created)
ENGINEERED_FEATURES = [
    "Temp_Difference",
    "Power_Watts",      # Derived from Torque and Speed
    "Tool_Wear_Bucket",
    "Operating_Band"
]

# Targets and Failure Modes
TARGET_COL = "Machine failure"

FAILURE_MODES = [
    "TWF", # Tool Wear Failure
    "HDF", # Heat Dissipation Failure
    "PWF", # Power Failure
    "OSF", # Overstrain Failure
    "RNF"  # Random Failures
]