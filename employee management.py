employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Amit', 'age': 30, 'department': 'IT', 'salary': 65000}
}


def add_employee():
    while True:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("❌ Employee ID already exists. Please enter a unique ID.")
        else:
            break

    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Employee Department: ")
    salary = float(input("Enter Employee Salary: "))

    employees[emp_id] = {
        'name': name,
        'age': age,
        'department': department,
        'salary': salary
    }

    print("✅ Employee added successfully!\n")


def view_employees():
    if not employees:
        print("⚠️ No employees available.\n")
        return

    print("\n{:<8} {:<15} {:<8} {:<15} {:<10}".format(
        "ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)

    for emp_id, details in employees.items():
        print("{:<8} {:<15} {:<8} {:<15} {:<10}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))
    print()


def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Found:")
        print(f"Name       : {emp['name']}")
        print(f"Age        : {emp['age']}")
        print(f"Department : {emp['department']}")
        print(f"Salary     : {emp['salary']}\n")
    else:
        print("❌ Employee not found.\n")


def main_menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("🙏 Thank you for using the Employee Management System!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.\n")

main_menu()
