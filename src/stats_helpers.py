"""
stats_helpers.py
Functions for hypothesis testing and statistical validation of failure modes.
"""
import pandas as pd
from scipy import stats

def run_ttest_on_failures(df: pd.DataFrame, feature: str, target_col: str) -> dict:
    """
    Runs an independent T-test to see if the mean of a continuous feature 
    is significantly different when a failure occurs.
    """
    # Split data into failed and healthy groups
    failed = df[df[target_col] == 1][feature]
    healthy = df[df[target_col] == 0][feature]
    
    # Perform Welch's T-test (assumes unequal variance)
    t_stat, p_val = stats.ttest_ind(failed, healthy, equal_var=False)
    
    return {
        "Feature": feature,
        "Failure_Mode": target_col,
        "Failed_Mean": round(failed.mean(), 2),
        "Healthy_Mean": round(healthy.mean(), 2),
        "P_Value": p_val,
        "Significant": p_val < 0.05
    }

def run_chi_square_test(df: pd.DataFrame, cat_col: str, target_col: str) -> dict:
    """
    Runs a Chi-Square test of independence between a categorical feature 
    and a binary failure flag.
    """
    # Create a contingency table
    contingency = pd.crosstab(df[cat_col], df[target_col])
    
    # Run test
    chi2, p_val, dof, expected = stats.chi2_contingency(contingency)
    
    return {
        "Category": cat_col,
        "Failure_Mode": target_col,
        "P_Value": p_val,
        "Significant": p_val < 0.05
    }