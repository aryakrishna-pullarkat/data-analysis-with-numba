import numpy as np
from numba import njit

@njit
def numba_outliers(arr):
    """
    Numba-accelerated IQR outlier detection.
    """
    Q1 = np.percentile(arr, 25)
    Q3 = np.percentile(arr, 75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    mask = (arr < lower) | (arr > upper)
    return mask

def detect_outliers(df):
    """
    Applies Numba outlier detection to ALL numeric columns.
    Removes rows containing outliers.
    """
    numeric_cols = df.select_dtypes(include='number').columns
    combined_mask = np.zeros(len(df), dtype=bool)

    for col in numeric_cols:
        arr = df[col].values.astype(np.float64)
        mask = numba_outliers(arr)
        combined_mask |= mask  # merge masks

    print(f"⚠ Found {combined_mask.sum()} outlier rows using Numba.")
    return df.loc[~combined_mask]  # keep only non-outliers
    
