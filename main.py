from functions.load_csv import load_csv
from functions.inspect_columns import inspect_columns
from functions.clean_duplicates import clean_duplicates
from functions.fix_column_names import fix_column_names
from functions.handle_missing import handle_missing
from functions.summary_stats import summary_stats
from functions.column_report import column_report
from functions.visualize_column import visualize_column
from functions.correlation_heatmap import correlation_heatmap
from functions.detect_outliers import detect_outliers
from functions.normalize_columns import normalize_columns
from functions.export_results import export_results

def main():
    df = load_csv()
    df = inspect_columns(df)
    df = clean_duplicates(df)
    df = fix_column_names(df)
    df = handle_missing(df)
    summary_stats(df)
    column_report(df)
    visualize_column(df)
    correlation_heatmap(df)
    df = detect_outliers(df)
    df = normalize_columns(df)
    export_results(df)

if __name__ == "__main__":
    main()