from employee import Employee
from salary import Salary
from attendance import Attendance
import os
from datetime import datetime


def display_info():
    directory = "employee_records"
    employee_id = input("Enter the employee ID you want to open: ")
    file_name = f"employee_{employee_id}.txt"
    file_path = os.path.join(directory, file_name)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            employee_data = file.read()
            print("Employee Information:")
            print(employee_data)
    else:
        print(f"Employee with ID {employee_id} not found.")


def display_all_employees():
    file_name = "employee_records.txt"

    try:
        with open(file_name, "r") as file:
            employee_data = file.read()
            print("Employee Information:")
            print(employee_data)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except PermissionError:
        print(f"Permission denied to access '{file_name}'.")


def remove_existing_id(employee_id):
    try:
        with open("existing_ids.txt", 'r') as file:
            existing_ids = set(map(int, file.read().split()))
        existing_ids.discard(employee_id)
        with open("existing_ids.txt", 'w') as file:
            file.write('\n'.join(map(str, existing_ids)))
    except FileNotFoundError:
        print("existing_ids.txt not found....")


def delete_employee_file(employee_id):
    filename = f"employee_records/employee_{employee_id}.txt"
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Employee file {filename} deleted.")


class Hrmis:

    def __init__(self):
        pass

    def update_employee(self):
        employee_id = input("Enter the employee ID of the user you want to edit")
        remove_existing_id(employee_id)
        self.delete_employee(employee_id)
        employee_id = int(input("New employee ID"))
        first_name = input("New first name")
        last_name = input("new last name")
        email = first_name + "." + last_name + "@mycompany.com"
        salary = input("New salary")

        Employee(employee_id, first_name, last_name, salary)

    def delete_employee(self, employee_id):
        confirm = input(f'Are you sure you want to delete Employee ID {employee_id}? (yes/no): ')

        if confirm.lower() == "yes":
            remove_existing_id(employee_id)
            delete_employee_file(employee_id)
            print(f"Employee ID {employee_id} has been deleted.")
        else:
            print("Deletion canceled.")

    def main(self):
        attendance_system = Attendance()

        while True:
            print("\n HRMIS Menu: ")
            print("1. Employee Management")
            print("2. Attendance Management")
            print("3. Salary Management")
            print("4. Exit")
            user_input = int(input("Enter your choice (1/2/3/4)"))

            if user_input == 1:
                print("\n HRMIS Menu: ")
                print("1. Add employee")
                print("2. Update employee")
                print("3. Remove Employee")
                print("4. Display employee")
                print("5. Display all employees information")
                print("6. Back")
                user_input2 = int(input("Enter your choice (1/2/3/4 \n"))

                if user_input2 == 1:
                    employee_id = int(input("Enter Employee ID: "))
                    first_name = input("Enter First Name: ")
                    last_name = input("Enter Last Name: ")
                    salary = float(input("Enter Salary: "))
                    Employee(employee_id, first_name, last_name, salary)
                    print("Employee added successfully.")
                elif user_input2 == 2:
                    self.update_employee()
                elif user_input2 == 3:
                    employee_id = int(input("Enter employee ID you want to delete"))
                    self.delete_employee(employee_id)
                elif user_input2 == 4:
                    display_info()
                elif user_input2 == 5:
                    display_all_employees()
                elif user_input2 == 6:
                    pass
                else:
                    print("Invalid choice. Please select a valid option.")
            elif user_input == 2:
                print("\nAttendance Management Menu:")
                print("1. Record Attendance ")
                print("2. Display individual attendance")
                print("3. Display all team attendance")
                print("4. Calculate working hours")
                print("5. Back")
                choice = input("Enter your choice (1/2/3): ")
                if choice == '1':
                    try:
                        employee_id = int(input("Enter Employee ID: "))
                        date = input("Enter Date (YYYY-MM-DD): ")
                        in_time = input("Enter In-Time (HH:MM): ")
                        out_time = input("Enter Out-Time (HH:MM): ")

                        datetime.strptime(date, "%Y-%m-%d")
                        datetime.strptime(in_time, "%H:%M")
                        datetime.strptime(out_time, "%H:%M")

                        attendance_system.record_attendance(employee_id, date, in_time, out_time)
                        print("Attendance recorded successfully.")
                    except ValueError:
                        print("Invalid input format. Please follow the specified format for employee ID, date, "
                              "in_time, and out_time.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                elif choice == '2':
                    employee_id = int(input("Enter Employee ID: "))
                    individual_attendance = attendance_system.get_employee_attendance(employee_id)
                    print(f"Attendance for Employee {employee_id}: {individual_attendance}")
                elif choice == '3':
                    all_attendance = attendance_system.get_all_employees_attendance()
                    print("All Employees' Attendance:")
                    for employee_id, records in all_attendance.items():
                        print(f"{employee_id}: {records}")

                elif choice == "4":
                    employee_id = int(input("Enter Employee ID: "))
                    start_date = input("Enter Start Date (YYYY-MM-DD): ")
                    end_date = input("Enter End Date (YYYY-MM-DD): ")
                    working_hours = attendance_system.calculate_working_hours(employee_id, start_date, end_date)
                    print(
                        f"Total working hours for Employee {employee_id} from {start_date} to {end_date}: {working_hours} hours")

                elif choice == "5":
                    pass
                else:
                    print("Invalid choice. Please select a valid option.")
            elif user_input == 3:
                print("\nSalary Management Menu:")
                print("1. Calculate Salary")
                print("2. Generate Pay Slip")
                print("3. Back")
                choice2 = input("Enter your choice (1/2/3): ")
                if choice2 == '1':
                    employee_id = int(input("Enter employee ID: "))
                    base_salary = int(input("Enter base salary"))
                    allowances = int(input("Enter allowances"))
                    bonuses = int(input("Enter bonuses"))
                    deductions = int(input("Enter deductions"))
                    salary = Salary(employee_id, base_salary, allowances, bonuses, deductions)
                    salary.display_salary()
                elif choice2 == '2':
                    employee_id = int(input("Enter employee ID: "))
                    base_salary = int(input("Enter base salary "))
                    allowances = int(input("Enter allowances "))
                    bonuses = int(input("Enter bonuses "))
                    deductions = int(input("Enter deductions "))
                    salary = Salary(employee_id, base_salary, allowances, bonuses, deductions)
                    salary.generate_pay_slip()
                elif choice2 == '3':
                    pass
                else:
                    print("Invalid choice. Please select a valid option.")
            elif user_input == 4:
                print("Closing the application")
                exit()


if __name__ == "__main__":
    hrmis = Hrmis()
    hrmis.main()
