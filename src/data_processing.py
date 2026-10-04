"""
data_processing.py
Contains functional data transformation pipelines for PlantPulse.
"""
import pandas as pd
import numpy as np

def engineer_temperature_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates heat dissipation capability (Process Temp - Air Temp)."""
    df = df.copy()
    # If this difference is too low, the machine isn't cooling properly.
    df['Temp_Difference [K]'] = df['Process temperature [K]'] - df['Air temperature [K]']
    return df

def engineer_power_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculates mechanical power in Watts.
    Physics formula: Power (W) = Torque (Nm) * Angular Velocity (rad/s)
    Angular Velocity = (Rotational speed [rpm] * 2 * pi) / 60
    """
    df = df.copy()
    angular_velocity = (df['Rotational speed [rpm]'] * 2 * np.pi) / 60
    df['Power [W]'] = df['Torque [Nm]'] * angular_velocity
    return df

def bucket_tool_wear(df: pd.DataFrame) -> pd.DataFrame:
    """Creates categorical buckets for tool wear to aid Power BI slicing."""
    df = df.copy()
    # Tool wear ranges from 0 to ~250 mins. Bucketing helps operations teams 
    # filter dashboards by machine lifecycle stages.
    bins = [-1, 60, 120, 180, 300]
    labels = ['New (0-60m)', 'Operational (61-120m)', 'Worn (121-180m)', 'Critical (181m+)']
    df['Tool_Wear_Bucket'] = pd.cut(df['Tool wear [min]'], bins=bins, labels=labels)
    return df

def run_feature_engineering_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """Executes the full feature engineering pipeline sequentially."""
    df = engineer_temperature_features(df)
    df = engineer_power_features(df)
    df = bucket_tool_wear(df)
    return df