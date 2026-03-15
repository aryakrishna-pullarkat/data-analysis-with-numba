def column_report(df):
    """
    Prints skewness, kurtosis, unique counts for numeric columns.
    """
    print("\n--- Column Report ---")
    num_cols = df.select_dtypes(include='number').columns

    for col in num_cols:
        print(f"\n📌 {col}:")
        print("  Unique:", df[col].nunique())
        print("  Min:", df[col].min())
        print("  Max:", df[col].max())
        print("  Skew:", df[col].skew())
        print("  Kurtosis:", df[col].kurt())