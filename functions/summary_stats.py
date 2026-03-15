import numpy as np
from numba import njit

@njit
def numba_summary(arr):
    """
    Computes mean, median, variance, std using Numba.
    """
    return np.array([
        arr.mean(),
        np.median(arr),
        arr.var(),
        arr.std()
    ])

def summary_stats(df):
    print("\n--- Summary Stats (Numba Accelerated) ---")
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        arr = df[col].values.astype(np.float64)
        mean_, median_, var_, std_ = numba_summary(arr)

        print(f"\n📌 {col}")
        print(f"  Mean   : {mean_}")
        print(f"  Median : {median_}")
        print(f"  Var    : {var_}")
        print(f"  Std    : {std_}")