import os
import matplotlib.pyplot as plt
import pandas as pd

def visualize_column(df):
    if df is None or df.empty:
        print("DataFrame is empty or invalid.")
        return

    while True:
        try:
            col = input("Enter column name to visualize: ").strip()

            if col not in df.columns:
                print("Column does not exist. Try again.")
                continue

            # Try converting to numeric
            df[col] = pd.to_numeric(df[col], errors='coerce')

            # Drop NaN values
            numeric_data = df[col].dropna()

            if numeric_data.empty:
                print("Column is not numeric or contains no valid numeric data. Try another column.")
                continue

            break

        except Exception as e:
            print("Invalid input. Please try again.")
            continue

    # Create plots directory if not exists
    os.makedirs("plots", exist_ok=True)

    # Histogram
    plt.figure()
    plt.hist(numeric_data, bins=10)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")
    hist_path = f"plots/{col}_histogram.png"
    plt.savefig(hist_path)
    plt.close()

    # Boxplot
    plt.figure()
    plt.boxplot(numeric_data)
    plt.title(f"Boxplot of {col}")
    box_path = f"plots/{col}_boxplot.png"
    plt.savefig(box_path)
    plt.close()

    print(f"Histogram saved at: {hist_path}")
    print(f"Boxplot saved at: {box_path}")
