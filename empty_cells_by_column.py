import pandas as pd


# Prompt user for file path
file_path = input("Enter the path of the CSV file: ")

# Load CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

# Check for empty cells in columns with available data
empty_cells_by_column = df[df.columns[df.isnull().sum() > 0]].isnull().sum()
print("Empty cells by column:")
print(empty_cells_by_column)