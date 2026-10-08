
# ============================================================
#              STUDENT MANAGEMENT SYSTEM
# ============================================================

students = {}


# ============================================================
# ADD STUDENT
# ============================================================

def add_student():
    print("\n--- Add Student ---")

    roll = input("Enter Roll Number: ")

    if roll in students:
        print("This roll number already exists!")
        return

    name = input("Enter Student Name: ")

    try:
        marks = float(input("Enter Marks (out of 100): "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    students[roll] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")


# ============================================================
# VIEW STUDENTS
# ============================================================

def view_students():
    print("\n--- Student List ---")

    if not students:
        print("No students found.")
        return

    print("-" * 50)
    print(f"{'Roll No.':<12}{'Name':<25}{'Marks':<10}")
    print("-" * 50)

    for roll, details in students.items():
        print(
            f"{roll:<12}"
            f"{details['name']:<25}"
            f"{details['marks']:<10.2f}"
        )

    print("-" * 50)


# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number: ")

    if roll in students:
        student = students[roll]
        print("Roll Number:", roll)
        print("Name:", student["name"])
        print("Marks:", student["marks"])
    else:
        print("Student not found.")


# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number: ")

    if roll not in students:
        print("Student not found.")
        return

    name = input("Enter New Name: ")

    try:
        marks = float(input("Enter New Marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    students[roll]["name"] = name
    students[roll]["marks"] = marks

    print("Student updated successfully!")


# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# ============================================================
# MAIN MENU
# ============================================================

def main_menu():
    while True:
        print("\n================================")
        print("     STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break
        else:
            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 6."
            )


# ============================================================
# START PROGRAM
# ============================================================

main_menu()
