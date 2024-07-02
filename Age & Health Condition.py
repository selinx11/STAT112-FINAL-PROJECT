# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Specify the file path for the Excel file
excel_path = r"C:\Users\Selin\Downloads\Cleanlenmis (1).xlsx"

# Attempt to read Excel file with a specific sheet name, catch exception and read without sheet name if necessary
try:
    df = pd.read_excel(excel_path, sheet_name='output(1)')
except ValueError:
    df = pd.read_excel(excel_path)

# Convert 'AGE' column to numeric values, coerce non-numeric values to NaN. Convert 'HEALTH_CONDITION' column to lowercase.
df['AGE'] = pd.to_numeric(df['AGE'], errors='coerce')
df['HEALTH_CONDITION'] = df['HEALTH_CONDITION'].str.lower()

# Drop rows with NaN values in 'AGE' or 'HEALTH_CONDITION' columns
df = df.dropna(subset=['AGE', 'HEALTH_CONDITION'])

# Define the order in which health conditions will be displayed in the violin plot
health_condition_order = ['fair', 'good', 'excellent']

# Set the size of the matplotlib figure
plt.figure(figsize=(12, 8))

# Define colors for the violin plot
colors = ['#287D8EFF', '#482677FF', '#73D055FF']

# Create a violin plot using Seaborn
sns.violinplot(x='HEALTH_CONDITION', y='AGE', data=df, order=health_condition_order, palette=colors)

# Set labels for the x-axis, y-axis, and the title of the plot
plt.xlabel('Health Condition')
plt.ylabel('Age')
plt.title('Do age and health condition have a directly proportional relationship?')

# Display the resulting violin plot
plt.show()