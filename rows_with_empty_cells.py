import pandas as pd

# Prompt user for file path
file_path = input("Enter the path of the CSV file: ")

# Load CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

# Filter rows with empty cells
rows_with_empty_cells = df[df.isnull().any(axis=1)]

# Display rows with empty cells
print(rows_with_empty_cells)
