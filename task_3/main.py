import pandas as pd
import glob


def merge_and_process_csvs(input_dir):
    """
    Merges multiple CSV files into a single DataFrame and performs basic aggregation.

    Args:
        input_dir: Path to the directory containing the CSV files.

    Returns:
        A summary DataFrame with aggregated results.
    """
    file_paths = glob.glob(f"{input_dir}/*.csv")

    if not file_paths:
        print(f"No CSV files found in {input_dir}")
        return None
    
    dataframes = []
    
    for file_path in file_paths:
        try:
            df = pd.read_csv(file_path)
            dataframes.append(df)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            continue

    if dataframes:
        combined_df = pd.concat(dataframes, ignore_index=True)

    return combined_df


def process_combined_data(df):
    """
    Processes the combined DataFrame, calculates aggregations, and returns a summary DataFrame.

    Args:
        df: The combined DataFrame.

    Returns:
        A summary DataFrame with aggregated results.
    """
    category_sums = df.groupby('category')['value'].sum()

    category_averages = df.groupby('category')['value'].mean()

    summary_df = pd.DataFrame({
        'Category': category_sums.index,
        'Total Value': category_sums.values,
        'Average Value': category_averages.values
    })
    return summary_df


if __name__ == "__main__":
    input_directory = "data/"
    output_file = "processed_data.csv"

    try:
        combined_df = merge_and_process_csvs(input_directory)
        if combined_df is not None:
            summary_df = process_combined_data(combined_df)
            summary_df.to_csv(output_file, index=False)
            print(summary_df)
    except Exception as e:
        print(f"An error occurred: {e}")