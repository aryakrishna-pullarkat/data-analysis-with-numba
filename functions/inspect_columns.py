def inspect_columns(df):
    """
    Prints dataset structure, dtypes, memory usage.
    """
    print("\n--- Dataset Overview ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    print("\nColumn Info:")
    print(df.dtypes)

    print("\nMemory Usage:")
    print(df.memory_usage(deep=True))

    print("\nFirst 3 Rows:")
    print(df.head(3))

    return df
