import argparse
import pandas as pd

def load_dataset(file_path):
    try:
        df = pd.read_csv(file_path)  # You can use other file formats if needed
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Load a dataset from a specified file.")
    parser.add_argument("file_path", type=str, help="Path to the dataset file")

    args = parser.parse_args()
    file_path = args.file_path

    df = load_dataset(file_path)

    if df is not None:
        # You can perform further processing or analysis on the loaded dataset here
        print("Dataset loaded successfully.")
        print(df.head())  # Example: Display the first few rows of the dataset

if __name__ == "__main__":
    main()

