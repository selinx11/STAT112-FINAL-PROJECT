# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Specify the file path for the Excel file
file_path = r"C:\Users\Selin\Downloads\Cleanlenmis (1).xlsx"

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Define income bins and labels for creating income bins
income_bins = list(range(30000, 110000, 10000)) + [101000]
income_labels = ['30k-40k', '40k-50k', '50k-60k', '60k-70k', '70k-80k', '80k-90k', '90k-100k', '100k-101k']

# Create a new column 'INCOME_BIN' with income bins based on the 'INCOME' column
df['INCOME_BIN'] = pd.cut(df['INCOME'], bins=income_bins, labels=income_labels)

# Define colors for different coverage levels
colors = {'Bronze': '#482677FF', 'Silver': '#73D055FF', 'Gold': '#287D8EFF'}

# Set the size of the matplotlib figure
plt.figure(figsize=(10, 6))

# Group the DataFrame by 'INCOME_BIN' and 'COVERAGE_LEVEL' and count the occurrences
grouped = df.groupby(['INCOME_BIN', 'COVERAGE_LEVEL']).size().unstack()

# Create a stacked bar plot using the grouped data and specified colors
grouped.plot(kind='bar', stacked=True, color=[colors[col] for col in grouped.columns])

# Set the title and labels for the plot
plt.title('Income Level vs Coverage Level')
plt.xlabel('Income Level')
plt.ylabel('Count')

# Rotate x-axis labels for better visibility
plt.xticks(rotation=45)

# Add a legend with a specified title
plt.legend(title='Coverage Level')

# Adjust layout for better appearance
plt.tight_layout()

# Display the resulting plot
plt.show()