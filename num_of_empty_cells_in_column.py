import pandas as pd

# Prompt user for file path
file_path = input("Enter the path of the CSV file: ")

# Load CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

# Replace empty cells with NaN
df.replace("", float("nan"), inplace=True)

# Prompt user for column name to check
column_name = input("Enter the column name to check: ")

# Check if column exists in DataFrame
if column_name not in df.columns:
    print(f"Column '{column_name}' not found in the CSV file.")
    exit()

# Count number of empty cells in the specified column
num_empty_cells = df[column_name].isna().sum()

# Print the count of empty cells in the specified column
print(f"Number of empty cells in column '{column_name}': {num_empty_cells}")
