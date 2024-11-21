import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "Updated_Gaming_Survey_Responses.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the dataset
print("Dataset Head:")
print(df.head())

# Basic Data Cleaning
df.columns = df.columns.str.strip()  # Remove leading/trailing whitespace
df.columns = df.columns.str.lower().str.replace(' ', '_')  # Normalize column names

# Summary of the dataset
print("\nDataset Info:")
print(df.info())

# Visualization: Age Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='age', data=df, palette='viridis', hue='age', dodge=False, legend=False)
plt.title('Age Distribution of Respondents')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()




# Visualization: Gender Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='gender', data=df, palette='coolwarm', hue='gender', dodge=False, legend=False)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


