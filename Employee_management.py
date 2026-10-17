
import json
import os

FILE_NAME = "employees.json"


def load_employees():
    """Load employee records from a JSON file."""
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read employee data.")
        return {}


def save_employees(employees):
    """Save employee records to a JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(employees, file, indent=4)
    except OSError:
        print("Error: Could not save employee data.")
        return False

    return True


def add_employee(employees):
    emp_id = input("Enter employee ID: ").strip()

    if not emp_id:
        print("Employee ID cannot be empty.")
        return

    if emp_id in employees:
        print("Employee ID already exists.")
        return

    name = input("Enter employee name: ").strip()
    department = input("Enter department: ").strip()

    try:
        age = int(input("Enter age: "))
        salary = float(input("Enter salary: "))

        if age <= 0 or salary < 0:
            print("Age must be positive and salary cannot be negative.")
            return
    except ValueError:
        print("Age must be an integer and salary must be numeric.")
        return

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    if save_employees(employees):
        print("Employee added successfully!")


def view_employees(employees):
    if not employees:
        print("No employees found.")
        return

    print("\n--- Employee List ---")

    for emp_id, details in employees.items():
        print(f"\nID: {emp_id}")
        print(f"Name: {details['name']}")
        print(f"Age: {details['age']}")
        print(f"Department: {details['department']}")
        print(f"Salary: {details['salary']:.2f}")


def search_employee(employees):
    emp_id = input("Enter employee ID to search: ").strip()

    employee = employees.get(emp_id)

    if employee is None:
        print("Employee not found.")
        return

    print(f"\nEmployee ID: {emp_id}")

    for key, value in employee.items():
        print(f"{key.title()}: {value}")


def update_employee(employees):
    emp_id = input("Enter employee ID to update: ").strip()

    if emp_id not in employees:
        print("Employee not found.")
        return

    print("1. Update name")
    print("2. Update age")
    print("3. Update department")
    print("4. Update salary")

    choice = input("Choose field: ").strip()

    if choice == "1":
        value = input("Enter new name: ").strip()
        if not value:
            print("Name cannot be empty.")
            return
        employees[emp_id]["name"] = value

    elif choice == "2":
        try:
            value = int(input("Enter new age: "))
            if value <= 0:
                print("Age must be positive.")
                return
            employees[emp_id]["age"] = value
        except ValueError:
            print("Invalid age.")
            return

    elif choice == "3":
        value = input("Enter new department: ").strip()
        if not value:
            print("Department cannot be empty.")
            return
        employees[emp_id]["department"] = value

    elif choice == "4":
        try:
            value = float(input("Enter new salary: "))
            if value < 0:
                print("Salary cannot be negative.")
                return
            employees[emp_id]["salary"] = value
        except ValueError:
            print("Invalid salary.")
            return

    else:
        print("Invalid choice.")
        return

    if save_employees(employees):
        print("Employee updated successfully!")


def delete_employee(employees):
    emp_id = input("Enter employee ID to delete: ").strip()

    if emp_id not in employees:
        print("Employee not found.")
        return

    confirm = input(
        f"Delete {employees[emp_id]['name']}? (yes/no): "
    ).strip().lower()

    if confirm != "yes":
        print("Deletion cancelled.")
        return

    employee = employees.pop(emp_id)

    if save_employees(employees):
        print("Employee deleted successfully!")
    else:
        # Restore the in-memory record if saving fails.
        employees[emp_id] = employee


def main():
    employees = load_employees()

    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            view_employees(employees)
        elif choice == "3":
            search_employee(employees)
        elif choice == "4":
            update_employee(employees)
        elif choice == "5":
            delete_employee(employees)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()






OUTPUT:

===== Employee Management System =====
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
Enter your choice: 1
Enter employee ID: E102
Enter employee name: Raj
Enter department: IT
Enter age: 24
Enter salary: 40000
Employee added successfully!

