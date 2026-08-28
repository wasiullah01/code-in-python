import pandas as pd 

data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan'],
    'Age': [20, 22, 21, 23],
    'City': ['Abbottabad', 'Islamabad', 'Lahore', 'Karachi'],
    'Score': [85, 90, 88, 92]
}

df = pd.DataFrame(data)

print(f"Data Frame: \n {df}")

column = df.loc[:4,'Name']
print(f"Names Only: \n{column}")

print(f"First Three Row: \n{df.head(3)}")
print(f"Last Row: \n {df.tail(1)}")

#specific student score
print(df.loc[2,'Score'])
