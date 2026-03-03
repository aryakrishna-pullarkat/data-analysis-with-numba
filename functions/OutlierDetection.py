import numpy as np
import pandas as pd


def detect_outliers(df: pd.DataFrame) -> pd.DataFrame:

    numeric_cols = df.select_dtypes(include=[np.number]).columns

    # If no numeric columns, return original
    if len(numeric_cols) == 0:
        print("No numeric columns found.")
        return df

    mask = np.ones(len(df), dtype=bool)

    for col in numeric_cols:
        col_series = df[col]
        col_values = col_series.values.astype(np.float64)

        valid_mask = ~np.isnan(col_values)
        if np.sum(valid_mask) == 0:
            continue

        lower, upper = iqr_bounds(col_values[valid_mask])

        col_mask = (col_series >= lower) & (col_series <= upper)
        mask &= col_mask | col_series.isna()

    removed_rows = len(df) - np.sum(mask)
    print(f"Removed {removed_rows} rows containing outliers.")

    return df[mask].reset_index(drop=True)
