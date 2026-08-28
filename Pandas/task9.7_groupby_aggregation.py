import pandas as pd

data = {
    'Subject': ['Math', 'Math', 'Physics', 'Physics', 'Chemistry', 'Chemistry'],
    'Name': ['Wasi', 'Ali', 'Sara', 'Khan', 'Zara', 'Hamza'],
    'Score': [85, 90, 88, 92, 87, 91]
}

df = pd.DataFrame(data)


#average per subject
avg_subj = df.groupby('Subject')['Score'].mean()
print(avg_subj)
print()




#highest score per subject
highest_score = df.groupby('Subject')['Score'].max()
print(highest_score)
print()

#lowest score per subject
lower_score = df.groupby('Subject')['Score'].min()
print(lower_score)
print()

#count student per subject
count_student = df.groupby('Subject')['Name'].count()
print(count_student)
print()

# Find subject with HIGHEST average
print("find a subject with highest subject")
highest_sub = avg_subj.idxmax()      #Returns subject NAME
highest_avg = avg_subj.max()         #Returns the value

print(f"Subject with highest average: {highest_sub} ({highest_avg:.2f})")


df.to_csv("Groups.csv")
print("CSV Saved")