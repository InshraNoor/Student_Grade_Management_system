student_grades = {  }
def add_student(stu_id, name, grade):
    student_grades[stu_id] = {"name": name, "grade": grade}
    print(f"Added {name} with ID {stu_id} and grade {grade}")

def update_student(stu_id, grade):
    if stu_id in student_grades:
        student_grades[stu_id]["grade"] = grade
        print(f"Student ID {stu_id} grade updated to {grade}")
    else:
        print("Student not found!")

def delete_student(stu_id):
    if stu_id in student_grades:
        del student_grades[stu_id]
        print(f"Student ID {stu_id} deleted successfully")
    else:
        print("Student not found!")

def display_all_students():
    if student_grades:
        for stu_id, info in student_grades.items():
            print(f"ID: {stu_id} | Name: {info['name']} | Grade: {info['grade']}")
    else:
        print("No students found/added")

def main():
    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter Your choice = "))
        if choice == 1:
            stu_id = input("Enter Student ID = ")
            name = input("Enter Student Name = ")
            grade = int(input("Enter Student Grade = "))
            add_student(stu_id, name, grade)

        elif choice == 2:
            stu_id = input("Enter Student ID = ")
            grade = int(input("Enter New Grade = "))
            update_student(stu_id, grade)

        elif choice == 3:
            stu_id = input("Enter Student ID = ")
            delete_student(stu_id)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")

main()