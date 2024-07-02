# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the cleaned data from an Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\Selin\Downloads\Cleanlenmis (1).xlsx")

# Set the size of the plotting figure
plt.figure(figsize=(10, 6))

# Create a boxplot using seaborn to visualize the relationship between 'COVERAGE_LEVEL' and 'AGE'
sns.boxplot(x='COVERAGE_LEVEL', y='AGE', data=df, palette='viridis')

# Set the title and axis labels for the plot
plt.title('Coverage Level/Age Relationship')
plt.xlabel('Coverage Level')
plt.ylabel('Age')

# Display the plot
plt.show()