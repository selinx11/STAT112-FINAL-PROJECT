# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\Selin\Downloads\Cleanlenmis (1).xlsx")

# Extract the 'YEAR' from the 'Date' column and create a new column
df['YEAR'] = df['Date'].dt.year

# Group the data by 'YEAR' and 'INSURANCE_TYPE', count the occurrences, and unstack the data
grouped_data = df.groupby(['YEAR', 'INSURANCE_TYPE']).size().unstack()

# Define light colors for the bar chart
light_colors = ['#287D8EFF', '#482677FF']

# Create subplots and plot the grouped data as a stacked bar chart
fig, ax = plt.subplots(figsize=(12, 8))
grouped_data.plot(kind='bar', stacked=True, ax=ax, color=light_colors)

# Set x-axis label, y-axis label, and plot title
ax.set_xlabel('Year')
ax.set_ylabel('Number of Claims')
ax.set_title('Insurance Types Over the Years')

# Display the plot
plt.show()