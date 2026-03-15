import numpy as np
from numba import njit
import warnings
warnings.filterwarnings("ignore", message="A value is trying to be set on a copy")
warnings.filterwarnings("ignore", message="inplace method will never work")

@njit
def numba_fill_mean(arr):
    """
    Replace NaN with column mean using Numba.
    """
    mean_val = np.nanmean(arr)
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            arr[i] = mean_val
    return arr

def handle_missing(df):
    """
    Handles missing values:
    - numeric: fill with mean (Numba accelerated)
    - categorical: fill with mode
    """
    print("\n--- Missing Value Handler (Numba for numeric) ---")

    for col in df.columns:
        if df[col].dtype != 'object':  # numeric
            arr = df[col].values.astype(np.float64)
            df[col] = numba_fill_mean(arr)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    print("Missing values filled!")
    return df
