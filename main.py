import json
import os

filename = "Students.json"
student_grades = {}

def load_data():
    global student_grades
    if os.path.exists(filename):
        with open(filename, "r") as f:
            student_grades = json.load(f)
    else:
        student_grades = {}

def save_data():
    with open(filename, "w") as f:
        json.dump(student_grades, f, indent=4)

def add_student(stu_id, name, grade):
    if stu_id in student_grades:
        print("This Student ID already exists! Try another ID")
    else:
        student_grades[stu_id] = {"name" : name, "grade" : grade}
        save_data()
        print(f"Added {name} with ID {stu_id} and grade {grade}")

def update_student(stu_id, grade):
    if stu_id in student_grades:
        student_grades[stu_id]["grade"] = grade
        save_data()
        print(f"Student ID {stu_id} grade updated to {grade}")
    else:
        print("Student Not Found")

def delete_student(stu_id):
    if stu_id in student_grades:
        del student_grades[stu_id]
        save_data()
        print(f"Student ID {stu_id} deleted Successfully!")
    else:
        print("Student Not Found!")

def display_all_students():
    if student_grades:
        print("\nID\t|\tName\t|\tGrade")
        print("--------|---------------|-------------")
        for stu_id, info in student_grades.items():
            print(f"{stu_id}\t|\t{info['name']}\t|\t{info['grade']}")
    else:
        print("No Student Found / Added")
    
def search_student(stu_id):
    if stu_id in student_grades:
        student = student_grades[stu_id]
        name = student["name"]
        grade = student["grade"]

        print("\nID\t|\tName\t|\tGrade")
        print("--------|---------------|-------------")
        print(f"{stu_id}\t|\t{name}\t|\t{grade}")
    else:
        print("Student not found!")


def main():
    load_data()

    while True:
        print("\n======Student Management System======")
        print("1. Add Student ")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Search Student")
        print("6. Exit\n")

        try:
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                stu_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                grade = int(input("Enter Student Grade: "))
                add_student(stu_id, name, grade)

            elif choice == 2:
                stu_id = input("Enter Student ID: ")
                grade = int(input("Enter New Grade: "))
                update_student(stu_id, grade)

            elif choice == 3:
                stu_id = input("Enter Student ID: ")
                delete_student(stu_id)

            elif choice == 4:
                display_all_students()
            
            elif choice == 5:
                stu_id = input("Enter Student ID: ")
                search_student(stu_id)

            elif choice == 6:
                print("Closing the Program.....")
                break

            else:
                print("Invalid Choice")


        except ValueError:
            print("Please Enter Numbers only!")

main()   