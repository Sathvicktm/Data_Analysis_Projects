import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Load the dataset
df = pd.read_csv('employee_salaries.csv')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows where 'salary' is missing
df = df.dropna(subset=['salary'])

# Optionally, fill missing values in other columns if needed
# df['department'].fillna('Unknown', inplace=True)

print("\nData after cleaning:")
print(df.head())

# Plot salary distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['salary'], kde=True, bins=30)
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Plot salary distribution by department
plt.figure(figsize=(12, 8))
sns.boxplot(x='department', y='salary', data=df)
plt.title('Salary Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Salary')
plt.xticks(rotation=45)
plt.show()

# Plot salary vs years of experience
plt.figure(figsize=(10, 6))
sns.scatterplot(x='years_of_experience', y='salary', data=df)
plt.title('Salary vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Display summary statistics of salary
print("\nSummary statistics of salary:")
print(df['salary'].describe())

# Calculate and display correlation between salary and years of experience
correlation = df[['salary', 'years_of_experience']].corr()
print("\nCorrelation between salary and years of experience:")
print(correlation)

# Perform simple linear regression analysis
# Define the predictor (X) and response variable (y)
X = df['years_of_experience']
y = df['salary']
X = sm.add_constant(X)  # Add a constant term to the predictor

# Fit the model
model = sm.OLS(y, X).fit()
print("\nLinear Regression Summary:")
print(model.summary())
