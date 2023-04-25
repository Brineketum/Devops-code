import pandas as pd

# Prompt user for file path
file_path = input("Enter the path of the CSV file: ")

# Load CSV file
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()
    
empty_cells = df.isnull().sum().sum()

if empty_cells > 0:
    print(f' There are {empty_cells} empty cells in the csv file')
else:
    print('There are no empty cells in the csv file,')