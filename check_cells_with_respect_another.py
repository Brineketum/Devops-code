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

# Prompt user for columns to check
column_a = input("Enter the name of column A: ")
column_b = input("Enter the name of column B: ")

# Check if column exists in DataFrame
if column_a or column_b not in df.columns:
    print(f"Column '{column_a}' not found in the CSV file.")
    exit()

# Prompt user for value to check against in first column A
value_to_check = input("Enter the value to check against in column A: ")

# Check if value of column A is equal to value_to_check and corresponding cell in column B is not empty
num_empty_cells = 0

all_ok = True;

# Check if value of column A is equal to value_to_check and corresponding cell in column B is not empty
for index, row in df.iterrows():
    if row[column_a] == value_to_check and pd.isna(row[column_b]):
        print(f"Empty cell at index {index} in column '{column_b}' with respect to the value '{value_to_check}' in column '{column_a}'.")
        all_ok = False;
        num_empty_cells += 1
        

if all_ok:
    print("There are no empty records with respect to the provided information")
# Print the count of empty cells in column B after the check
print(f"Number of empty cells in column '{column_b}' after checking against value '{value_to_check}' in column '{column_a}': {num_empty_cells}")