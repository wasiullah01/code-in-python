import pandas as pd

data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Zara'],
    'Age': [20, 22, 21, 23, 19],
    'Score': [85, 90, 88, 92, 87]
}

df = pd.DataFrame(data)

high_scorers = df[df['Score'] > 88]
print(high_scorers)

older_students = df[df['Age'] > 21]
print(older_students)

result = df[(df['Score'] > 85) & (df['Age'] >= 22)]
print(result)

print(f"Average Score: {df['Score'].mean()}")
print(f"Highest Score: {df['Score'].max()}")
print(f"Lowest Score: {df['Score'].min()}")
print(f"Total Students: {len(df)}")

print(f"Students aged 20+: {len(df[df["Age"] >= 20])}")

sorted_df = df.sort_values('Score', ascending=False)
print(sorted_df)
