total_students = int(input("How many students do you want to enter?: "))
students = []

subjects = ["Eng","Math","Bio"]
grade = []

for i in range(total_students):
    
    list_std = {}
    list_std["name"] = input(f"Enter Student{i+1} name: ")
    list_std["age"] = int(input(f"Enter Student{i+1} age: "))
    list_std["subject"] = input(f"Enter Student{i+1} Favorit Subject : ")
    list_std["score"] = tuple(map(int, input(f"Enter {subjects} seperated by space: ").split()))
    list_std["maximum"] = max(list_std["score"])
    list_std["minimum"] = min(list_std["score"])
    list_std["average"] = sum(list_std["score"])/3

    #grade loop
    if list_std["average"] >= 90:
        grade = "A"
    elif list_std["average"] >= 80:
        grade = "B"    
    elif list_std["average"] >= 70:
            grade = "C"
    elif list_std["average"] >= 50:
            grade = "D"
    elif list_std["average"] < 50:
            grade = "F"

    list_std["grade"] = grade
    #put all dict data into a students list
    students.append(list_std)

for i,std in enumerate(students,1):
      print(f"---Student {i}--- ")
      print(f"Name : {std["name"]}")
      print(f"Age : {std["age"]}")
      print(f"Score : {std["score"]}")
      print(f"Average : {std["average"]}")
      print(f"Highest : {std["maximum"]}")
      print(f"Lowest : {std["minimum"]}")
      print(f"Grade: {std["grade"]}")
      print(f"Fav Subject: {std["subject"]}")
