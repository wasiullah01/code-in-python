import pandas as pd

# Data with problems (missing values, duplicates)
data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Ali', None],
    'Age': [20, 22, None, 23, 22, 25],
    'Score': [85, 90, 88, 92, 90, None]
}

df = pd.DataFrame(data)

#show orignal data
print(df)

#count missing values per column
print(df.isnull().sum())

#remove row with missing values
print("remove row missig values: ")
print(df.dropna())

print("remove dup rows:")
dup_row = df.drop_duplicates()
print(dup_row)

print("Fill missing with average")
avg = df['Score'].mean()
age = df['Age'].mean()
fill_missing = df.fillna({'Name': "Hamza", 'Score': avg, 'Age': age})
print(fill_missing)

fill_missing.to_csv("Clean_Data.csv", index=True)
print("Clean data saved: File name : Clean_Data.csv")




