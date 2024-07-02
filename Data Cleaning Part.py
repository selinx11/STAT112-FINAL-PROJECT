# Import necessary libraries
import pandas as pd
import numpy as np

# Read Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\Users\Selin\Desktop\Insurance.xlsx")

# Rename columns using the provided dictionary
dict = {'Data Description : The dataset consists of 121 observations and 11 variables': 'YEAR',
        'Unnamed: 1': 'MONTH',
        'Unnamed: 2': 'AGE',
        'Unnamed: 3': 'GENDER',
        'Unnamed: 4': 'INCOME',
        'Unnamed: 5': 'INSURANCE_TYPE',
        'Unnamed: 6': 'COVERAGE_LEVEL',
        'Unnamed: 7': 'HEALTH_CONDITION',
        'Unnamed: 8': 'DOCTOR_VISITS',
        'Unnamed: 9': 'PREMIUM_AMOUNT',
        'Unnamed: 10': 'CLAIMS'}
df.rename(columns=dict, inplace=True)

# Remove the first two rows from the DataFrame
n = 2
df.drop(index=df.index[:n], inplace=True)

# Calculate the median age and replace missing values in the 'AGE' column
median_age = int(df['AGE'].median())
df['AGE'] = df["AGE"].astype(str)
df['AGE'] = df['AGE'].str.lstrip("-")
df["AGE"] = df["AGE"].str.replace('nan', str(median_age))
df['AGE'] = df["AGE"].astype(float)

# Replace 'Female' with 'F' and 'Male' with 'M' in the 'GENDER' column
df['GENDER'] = df['GENDER'].str.replace("Female", "F")
df['GENDER'] = df['GENDER'].str.replace("Male", "M")

# Calculate the mode of the 'GENDER' column and replace missing values
mode_gender = df['GENDER'].mode()
df['GENDER'] = df['GENDER'].str.replace("nan", str(mode_gender))

# Calculate the median income and replace missing values in the 'INCOME' column
median_Income = int(df['INCOME'].median())
df['INCOME'] = df['INCOME'].astype(str)
df['INCOME'] = df['INCOME'].str.replace('nan', str(median_Income))
df['INCOME'] = df['INCOME'].astype(float)

# Calculate the mode of the 'INSURANCE_TYPE' column and replace missing values
mode_insurance = df['INSURANCE_TYPE'].mode()
df['INSURANCE_TYPE'] = df['INSURANCE_TYPE'].str.replace('NA', str(mode_insurance))

# Fill missing values in various columns with their respective modes
df['GENDER'].fillna(df['GENDER'].mode()[0], inplace=True)
df['INSURANCE_TYPE'].fillna(df['INSURANCE_TYPE'].mode()[0], inplace=True)
df['COVERAGE_LEVEL'].fillna(df['COVERAGE_LEVEL'].mode()[0], inplace=True)
df['HEALTH_CONDITION'].fillna(df['HEALTH_CONDITION'].mode()[0], inplace=True)

# Capitalize values in the 'COVERAGE_LEVEL' column
df["COVERAGE_LEVEL"] = df["COVERAGE_LEVEL"].str.capitalize()

# Fill missing values in the 'CLAIMS' column with the median
median_claims = df['CLAIMS'].median()
df['CLAIMS'].fillna(median_claims, inplace=True)
df['CLAIMS'] = df['CLAIMS'].astype(str)
df['CLAIMS'] = df['CLAIMS'].str.lstrip("-")

# Clean and convert data types in the 'PREMIUM_AMOUNT' column
df['PREMIUM_AMOUNT'] = df['PREMIUM_AMOUNT'].astype(str)
df['PREMIUM_AMOUNT'] = df['PREMIUM_AMOUNT'].str.rstrip("00")
df['PREMIUM_AMOUNT'] = df['PREMIUM_AMOUNT'].str.replace(',', '').astype(float)

# Fill missing values in the 'PREMIUM_AMOUNT' column with the median
median_premium = df['PREMIUM_AMOUNT'].median()
df['PREMIUM_AMOUNT'].fillna(median_premium, inplace=True)

# Clean and convert data types in the 'DOCTOR_VISITS' column
df['DOCTOR_VISITS'] = df['DOCTOR_VISITS'].astype(str)
df['DOCTOR_VISITS'] = df['DOCTOR_VISITS'].str.replace('six', '6').astype(float)

# Fill missing values in the 'DOCTOR_VISITS' column with the median
median_doctor = df['DOCTOR_VISITS'].median()
df['DOCTOR_VISITS'].fillna(median_doctor, inplace=True)

# Map abbreviated month names to full names and create a 'Date' column
month_mapping = {'Jan': 'january', 'Feb': 'february', 'Mar': 'march', 'Apr': 'april', 'May': 'may', 'Jun': 'june',
                 'Jul': 'july', 'Aug': 'august', 'Sep': 'september', 'Oct': 'october', 'Nov': 'november', 'Dec': 'december'}
df['MONTH'] = df['MONTH'].map(month_mapping)
df['Date'] = df['YEAR'].astype(str) + ' ' + df['MONTH']

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%Y %B')

# Print the cleaned DataFrame
print(df)

# Save the cleaned data to a new Excel file without including the index column
df.to_excel('CleanedData.xlsx', index=False)