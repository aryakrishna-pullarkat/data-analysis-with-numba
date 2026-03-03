import numpy as np
from numba import njit

@njit
def numba_minmax(arr):
    return (arr - arr.min()) / (arr.max() - arr.min())

@njit
def numba_zscore(arr):
    return (arr - arr.mean()) / arr.std()

def normalize_columns(df):
    """
    Applies min-max scaling & z-score normalization (Numba accelerated)
    """
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        arr = df[col].values.astype(np.float64)
        df[col + "_minmax"] = numba_minmax(arr)
        df[col + "_zscore"] = numba_zscore(arr)

    print("⚡ Normalized columns using Numba (min-max + z-score)")
    return df

