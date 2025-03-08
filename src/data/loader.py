# src/data/loader.py
import pandas as pd
import os


def load_data(filepath):
    """
    Loads data from a CSV file into a pandas DataFrame.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded DataFrame, or None if an error occurs.
    """
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Example usage (replace with your actual file path)
    filepath = r"C:\Users\neba\Documents\week-3\MachineLearningRating_v3.csv"  # Make sure to use raw strings for windows paths.

    if os.path.exists(filepath):
        loaded_df = load_data(filepath)

        if loaded_df is not None:
            print("Data loaded successfully.")
            print("First 5 rows:")
            print(loaded_df.head())
            print("\nDataFrame info:")
            print(loaded_df.info())
        else:
            print("Data loading failed.")
    else:
        print(f"The file {filepath} does not exist.")
