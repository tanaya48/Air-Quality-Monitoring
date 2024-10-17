# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the air quality dataset - make sure the file path is correct!
df = pd.read_csv('airquality.csv')  # Update with correct path if needed

# View the first few rows of the dataset to understand its structure
print("Original Data:")
print(df.head())

# --- Data Cleaning: Handling Missing Values ---

# Check for missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Fill missing values with the mean of the respective columns
df.fillna(df.mean(), inplace=True)

# Check for missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# --- Pie Chart: Distribution of 'Ozone' Levels ---
# Categorize 'Ozone' levels for pie chart visualization
df['Ozone_Category'] = pd.cut(df['Ozone'], bins=[0, 20, 40, 60, 100, 200], labels=['Very Low', 'Low', 'Moderate', 'High', 'Very High'])

plt.figure(figsize=(8, 6))
ozone_counts = df['Ozone_Category'].value_counts()
plt.pie(ozone_counts, labels=ozone_counts.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
plt.title('Ozone Level Distribution')
plt.show()

# --- Box Plot: Wind Speed and Temperature ---
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[['Wind', 'Temp']], palette="Set2")
plt.title('Box Plot of Wind Speed and Temperature')
plt.show()

# --- Scatter Plot: Ozone vs Wind ---
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Ozone', y='Wind', data=df, hue='Ozone_Category', palette='coolwarm')
plt.title('Scatter Plot of Ozone vs Wind Speed')
plt.show()

# --- Heat Map: Correlation Between Variables ---
plt.figure(figsize=(10, 8))
corr_matrix = df[['Ozone', 'Solar.R', 'Wind', 'Temp']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Heat Map of Variable Correlations')
plt.show()
