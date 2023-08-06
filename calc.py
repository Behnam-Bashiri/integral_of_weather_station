import pandas as pd
from scipy.integrate import trapz

# Function to read data from CSV file
def read_data_from_csv(file_path, x_column, y_column):
    df = pd.read_csv(file_path)
    x_values = df[x_column].to_numpy().astype(float)
    y_values = df[y_column].to_numpy().astype(float)
    return x_values, y_values


# Temp 1
# Example usage:
file_path = 'temp1.csv'  # Replace with your CSV file path.
x_column = 'x'  # Replace 'time' with the column name for x-coordinates (time or string time).
y_column = 'y'  # Replace 'value' with the column name for y-coordinates.

x_values, y_values = read_data_from_csv(file_path, x_column, y_column)

result1 = (trapz(y_values, x_values)*1.976)

file_path = 'temp2.csv'  # Replace with your CSV file path.
x_column = 'x'  # Replace 'time' with the column name for x-coordinates (time or string time).
y_column = 'y'  # Replace 'value' with the column name for y-coordinates.

x_values, y_values = read_data_from_csv(file_path, x_column, y_column)

result2 = (trapz(y_values, x_values)*1.976)
print("Temp 2 : Discrete Integration Result:", result2)
print("Temp 1 : Discrete Integration Result:", result1)
print("sum",(result2)/60)
