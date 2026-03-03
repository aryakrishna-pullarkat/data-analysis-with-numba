import numpy as np
from numba import njit


@njit
def iqr_bounds(values):
    sorted_vals = np.sort(values)
    n = len(sorted_vals)

    q1 = sorted_vals[int(0.25 * (n - 1))]
    q3 = sorted_vals[int(0.75 * (n - 1))]

    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return lower, upper
