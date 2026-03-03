import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):
    numeric_df = df.apply(pd.to_numeric, errors='coerce')
    numeric_df = numeric_df.dropna(axis=1, how='all')

    if numeric_df.shape[1] == 0:
        print("No numeric columns available for correlation.")
        return

    corr_matrix = numeric_df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()