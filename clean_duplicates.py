def clean_duplicates(df):
    duplicate_count = df.duplicated().sum()
    print("Duplicate rows found:", duplicate_count)

    df_cleaned = df.drop_duplicates()

    print("Duplicates removed:", duplicate_count)
    return df_cleaned