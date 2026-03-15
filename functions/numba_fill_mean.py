import numpy as np
from numba import njit
import warnings
warnings.filterwarnings("ignore", message="A value is trying to be set on a copy")
warnings.filterwarnings("ignore", message="inplace method will never work")

@njit
def numba_fill_mean(arr):
    mean_val = np.nanmean(arr)
    for i in range(len(arr)):
        if np.isnan(arr[i]):
            arr[i] = mean_val
    return arr
