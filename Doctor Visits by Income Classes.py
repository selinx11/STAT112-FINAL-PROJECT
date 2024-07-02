# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Define the path to the Excel file
excel_path = r"C:\Users\Selin\Downloads\Cleanlenmis (1).xlsx"

# Try reading the Excel file with a specific sheet name, handle ValueError if the sheet doesn't exist
try:
    df = pd.read_excel(excel_path, sheet_name='output(1)')
except ValueError:
    df = pd.read_excel(excel_path)

# Convert the 'DOCTOR_VISITS' column to numeric, handling errors by coercing to NaN
df['DOCTOR_VISITS'] = pd.to_numeric(df['DOCTOR_VISITS'], errors='coerce')

# Define income bins and labels for creating income classes
income_bins = [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000, 110000]
income_labels = ['30k-40k', '40k-50k', '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-100k', '100k-110k']

# Create a new column 'Income Classes' by binning the 'INCOME' column
df['Income Classes'] = pd.cut(df['INCOME'], bins=income_bins, labels=income_labels, right=False)

# Group by 'Income Classes' and calculate the mean of 'DOCTOR_VISITS'
average_premium_by_income = df.groupby('Income Classes')['DOCTOR_VISITS'].mean()

# Define a color for the bar chart
color = '#287D8EFF'

# Create a bar chart with specified attributes
plt.figure(figsize=(10, 6))
bars = plt.bar(average_premium_by_income.index, average_premium_by_income, color=color, edgecolor='black', alpha=0.7)
plt.xlabel('Income Classes')
plt.ylabel('DOCTOR_VISITS')
plt.title('Doctor Visits by Income Classes')

# Add a color bar and remove it (for aesthetics in this case)
cbar = plt.colorbar(plt.cm.ScalarMappable(cmap='Blues'), ax=plt.gca())
cbar.remove()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Display the plot
plt.show()