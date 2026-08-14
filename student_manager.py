
import sys


def display():
    print("--Student Manager--\n")
    print("1: Add Student \n")
    print("2: View Students\n")
    print("3: Exit \n")
    select = int(input("Enter Your Choice Here! "))
    return select

def add_std():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    email = input("Enter Email: ")
    gpa = float(input("Enter GPA: "))


    with open("student.txt", "a") as file:
        file.write(f"Name: {name}, \n Age: {age},\nEmail: {email},\n GPA: {gpa}\n")
        print("Student added successfully\n")

def view_std():
    try:
        with open("student.txt", "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No content Found")
    except FileNotFoundError:
        print("No Student Found \n")

def exit():
    print("Exiting...")
    sys.exit()


def main():

    while True:
        choice = display()

        if choice == 1:
            add_std()
        elif choice == 2:
            view_std()
        elif choice == 3:
            exit()
        else: 
            print("Please select within range")
             



 


