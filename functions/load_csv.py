import pandas as pd
import os

def load_csv():

    while True:
        path = "imdb_top_1000.csv"

        if not os.path.exists(path):
            print("❌ File not found. Try again.")
            continue

        try:
            df = pd.read_csv(path)
            print("✅ CSV loaded successfully!")
            return df
        except Exception as e:
            print("❌ Failed to load CSV:", e)
