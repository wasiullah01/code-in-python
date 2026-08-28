import pandas as pd

data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Zara'],
    'Age': [20, 22, 21, 23, 19],
    'Score': [85, 90, 88, 92, 87]
}


df = pd.DataFrame(data)

print(df[df['Score'] > 87])

print(df[df['Age'] >= 22])

print(df[(df['Score'] > 85) & (df['Age'] >= 21)])

print(f"Average: {df['Score'].mean()}")
print(f"Max: {df['Score'].max()}")
print(f"Min: {df['Score'].min()}")

print(len(df))

high_score = df.sort_values('Score', ascending=False)
print( high_score)


