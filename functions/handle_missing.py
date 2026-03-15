def handle_missing(df):
    print("\n--- Missing Value Handler (Numba for numeric) ---")

    for col in df.columns:
        if df[col].dtype != 'object': 
            arr = df[col].values.astype(np.float64)
            df[col] = numba_fill_mean(arr)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    print("Missing values filled!")
    return df
