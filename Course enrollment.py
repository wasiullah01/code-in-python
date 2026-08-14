
#week 3 milestone

def faculty(courseID):
    teachers = {
      1 : "Attiq",
      2 : "Zahid",
      3 : "Dr Fahad",
      4 : "Ghassan",
    }

    if courseID == 1:
          print(f"Congrat! You are new instructor for Data Structure is:  Mr.{teachers[1]}")

    elif courseID == 2:
          print(f"Congrat! You are new instructor Operating System: Mr.{teachers[1]}")
    elif courseID == 3:
           print(f"Congrat! You are new instructor Digital Marketing Mr.{teachers[2]}")

    elif courseID == 4:
           print(f"Congrat! You are new instructor Database Mr.{teachers[2]}")
    elif courseID == 5:
           print(f"Congrat! You are new instructor net security  Mr.{teachers[4]}")
    elif courseID == 6:
           print(f"Congrat! You are new instructor cybersec Mr.{teachers[4]}")
    elif courseID == 7:
           print(f"Congrat! You are new instructor python for beg Mr.{teachers[3]}")
    elif courseID == 8:
           print(f"Congrat! You are new instructor graphic design Mr.{teachers[3]}")
        
    



def subjects():
    courses = {
     1 : "Data Structure",
     2 : "Operating system",
     3 : "Digital Marketing",
     4 : "Database",
     5 : "Network Security",
     6 : "Cyber Security",
     7 : "python for begginners",
     8 : "Graphic Design"
    }

    print("Which course do you want to enroll, Enter course code: ")

    for key,course in courses.items():
              print(f"{key} {course}")

    std_course = int(input("Please Enter the course code here: "))
          

    if std_course in courses:
          return std_course
    else:
          print("Invalid")
          return subjects()


                                


def students():
    student = []

    std = {}
    std["Name"] = input("Enter your name: ")
    std["Father Name"] = input("Enter your Father Name: ")
    std["Age"] = int(input("Enter your Age: "))
    std["phone num"] = int(input("Enter your phone number: "))
    std["email"] = input("Enter your email: ")
    student.append(std)
    return student 




student_data = students()

course_id = subjects()

faculty(course_id)
