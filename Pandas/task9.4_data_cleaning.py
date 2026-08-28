import pandas as pd 
import numpy as np 

# Data with problems (missing values, duplicates)
data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Ali', None],
    'Age': [20, 22, None, 23, 22, 25],
    'Score': [85, 90, 88, 92, 90, None]
}

df = pd.DataFrame(data)

print("Orignal Data: ")
print(df)
print()

#check missing value

print("Missing Values: ")
print(df.isnull())
print()

#Count missing Values
print("Count missing per column: ")
print(df.isnull().sum())
print()

#Drop rows with ANY missing values
clean_df = df.dropna()
print("After Dropna(): ")
print(clean_df)
print()

#drop entire row is missing
clean_df2 = df.dropna(how='all')
print("After dropna(how='all':) ")
print(clean_df2)
print()

#fill missing values with a value
fill_df = df.fillna({'Name': "Hamza", 'Age': 21,'Score':85})
print("After fillna():")
print(fill_df)
print()

#show dublicate
print("Show Duplicate: ")
print(df[df.duplicated()])
print()

#drop duplicate
print("Drop Duplicate: ")
no_dup = df.drop_duplicates()
print(no_dup)