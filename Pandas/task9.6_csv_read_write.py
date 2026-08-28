# Create messy student data (with missing values, duplicates)
# Clean the data (remove missing, duplicates, fill averages)
# Save cleaned data to CSV (students_cleaned.csv)
# Read the CSV back into a new DataFrame
# Show statistics from the cleaned data
# Save a summary report to text file
import pandas as pd 

data = {
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Ali', None],
    'Age': [20, 22, None, 23, 22, 25],
    'Score': [85, 90, 88, 92, 90, None]
}

df = pd.DataFrame(data)
print("Student Data Summary")
print("="*20 )
score_avg = df['Score'].mean()
age_avg = df["Age"].mean()

fill_average = df.fillna({'Score': score_avg, 'Age': age_avg})
remove_missing = fill_average.dropna().drop_duplicates()

remove_missing.to_csv("Student_Cleaned.csv", index=False)
print()
print(remove_missing)
df_read = pd.read_csv("Student_Cleaned.csv")
print(f"Average Score: {remove_missing['Score'].mean()}")
print(f"Total Students: {len(remove_missing)}")

with open("Student_clean.txt", 'w') as file:
    file.write(f"Data: {remove_missing}\n")
    file.write(f"Average Score: {score_avg}\n")
    file.write(f"Total Student: {len(remove_missing)}\n")

print("File saved Student_clean.txt")
