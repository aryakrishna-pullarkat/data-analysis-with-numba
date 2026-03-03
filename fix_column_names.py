def fix_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    print("Column names cleaned.")
    print("Column names standardized:", df.columns.tolist())
    return df