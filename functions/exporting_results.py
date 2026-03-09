import pandas as pd

def export_results(df):
    df.to_csv("cleaned_data.csv", index=False)
    
    with open("report.txt", "w") as report:
        report.write("DATASET REPORT\n")
        report.write("=" * 40 + "\n\n")
        report.write(f"Total Rows: {df.shape[0]}\n")
        report.write(f"Total Columns: {df.shape[1]}\n")
        report.write("Column Names:\n")
        
        for col in df.columns:
            report.write(f"- {col}\n")
        
        report.write("\nDataset Summary:\n")
        report.write(str(df.describe(include='all')))
    
    print("Files 'cleaned_data.csv' and 'report.txt' created successfully.")
