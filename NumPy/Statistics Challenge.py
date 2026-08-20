import numpy as np 

arr = np.random.randint(0,100, 50)
print(arr)

print(f"Mean: {np.mean(arr)}")
print(f"Sum: {np.sum(arr)}")
print(f"Median: {np.median(arr)}")
print(f"Standard Deviation: {np.std(arr)}")
print(f"Varience: {np.var(arr)}")

print(f"Percentile 25th: {np.percentile(arr,25)}")
print(f"Percentile 50th: {np.percentile(arr,50)}")
print(f"Percentile 75th: {np.percentile(arr,75)}")

grade_A = arr[arr >= 90]
print("Grade A")
print(grade_A)

grade_B = arr[(arr >= 80) & (arr < 90)]
print("Grade B")
print(grade_B) 

grade_C = arr[(arr >= 70) & (arr < 80)]
print("Grade C")
print(grade_C)

grade_D = arr[arr < 70]
print(" Grade D")
print(grade_D)

with open("grade_statistics.txt", "w") as file:
    file.write("TEST SCORE STATISTICS REPORT\n")
    file.write("=" * 25 + "\n\n")
    file.write(f"Total Students: {len(arr)}\n")
    file.write(f"Mean: {np.mean(arr):.2f}\n")
    file.write(f"Median: {np.median(arr):.2f}\n")
    file.write(f"Std Dev: {np.std(arr):.2f}\n")
    file.write(f"Varience: {np.var(arr):.2f}\n")
    file.write(f"Percentile 25th: {np.percentile(arr,25)}\n")
    file.write(f"Percentile 50th: {np.percentile(arr,50)}\n")
    file.write(f"Percentile 75th: {np.percentile(arr,75)}\n\n")
    file.write(f"Grade A (90-100): {len(grade_A)}\n")
    file.write(f"Grade B (80-89): {len(grade_B)}\n")
    file.write(f"Grade C (70-79): {len(grade_C)}\n")
    file.write(f"Grade D (Below 70): {len(grade_D)}\n")


print("Report saved ")

