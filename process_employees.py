import pandas as pd

df = pd.read_csv("employees.csv")

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove decimal places from Age column
df['Age'] = df['Age'].astype(int)

# 3. Convert USD salary to EGP (Assuming an exchange rate of 30.5)
exchange_rate = 30.5
df['Salary EGP'] = df['Salary US'] * exchange_rate

# 4. Print statistics
print("Average Age:", df['Age'].mean())
print("Median Salary:", df['Salary EGP'].median())
print("Ratio between males and female employees:", df['Gender'].value_counts()['M'] / df['Gender'].value_counts()['F'])

# 5. Write data to a new CSV file
df.to_csv("processed_employees.csv", index=False)