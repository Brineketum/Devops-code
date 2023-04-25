import pandas as pd

# Prompt user for file path
file_path = input("Enter the path of the CSV file: ")

# Load CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

# Prompt user for column name
column_name = input("Enter the column name to check datatype for: ")

# Check if column exists in DataFrame
if column_name not in df.columns:
    print(f"Column '{column_name}' not found in the CSV file.")
    exit()

# Prompt user for expected datatype
expected_dtype = input("Enter the expected datatype for the column: ")

# Get datatype of each cell in the column
column_dtype = df[column_name].apply(type)

# Count matches and mismatches
matches = (column_dtype == expected_dtype).sum()
mismatches = (column_dtype != expected_dtype).sum()

# Display results
print("Results:")
print(f"Total cells in column '{column_name}': {len(df)}")
print(f"Cells with expected datatype '{expected_dtype}': {matches}")
print(f"Cells with mismatched datatype: {mismatches}")
