# from employee import Employee
# from salary import Salary
# from attendance import Attendance
# import os
# from datetime import datetime
#
#
# def update_employee(employee_id = None):
#     employee_id = input("Enter the employee ID of the user you want to edit")
#     remove_existing_id(employee_id)
#     delete_employee(employee_id)
#     employee_id = int(input("New employee ID"))
#     first_name = input("New first name")
#     last_name = input("new last name")
#     email = first_name + "." + last_name + "@mycompany.com"
#     salary = input("New salary")
#
#     Employee(employee_id, first_name, last_name, salary)
#
#
# def delete_employee(employee_id):
#     # Confirm the deletion with the user
#     confirm = input(f'Are you sure you want to delete Employee ID {employee_id}? (yes/no): ')
#
#     if confirm.lower() == "yes":
#         # Remove the employee's ID from the "existing_ids.txt" file
#         remove_existing_id(employee_id)
#
#         # Delete the file associated with this employee
#         delete_employee_file(employee_id)
#
#         print(f"Employee ID {employee_id} has been deleted.")
#     else:
#         print("Deletion canceled.")
#
#
# def remove_existing_id(employee_id):
#     try:
#         with open("existing_ids.txt", 'r') as file:
#             existing_ids = set(map(int, file.read().split()))
#         existing_ids.discard(employee_id)
#         with open("existing_ids.txt", 'w') as file:
#             file.write('\n'.join(map(str, existing_ids)))
#     except FileNotFoundError:
#         print("existing_ids.txt not found....")
#
#
# def delete_employee_file(employee_id):
#     filename = f"employee_records/employee_{employee_id}.txt"
#     if os.path.exists(filename):
#         os.remove(filename)
#         print(f"Employee file {filename} deleted.")
#
#
# def main():
#     while True:
#
#         print("\n HRMIS Menu: ")
#         print("1. Employee Management")
#         print("2. Attendance Management")
#         print("3. Salary Management")
#         print("4. Exit")
#         user_input = int(input("Enter your choice (1/2/3/4)"))
#
#         if user_input == 1:
#             print("\n HRMIS Menu: ")
#             print("1. Add employee")
#             print("2. Update employee")
#             print("3. Remove Employee")
#             print("4. Back")
#             user_input2 = int(input("Enter your choice (1/2/3/4 \n"))
#
#             if user_input2 == 1:
#                 # Add Employee
#                 # Prompt the user for employee details and call the relevant methods from the Employee class.
#                 employee_id = int(input("Enter Employee ID: "))
#                 first_name = input("Enter First Name: ")
#                 last_name = input("Enter Last Name: ")
#                 salary = float(input("Enter Salary: "))
#                 email = first_name + "." + last_name + "@mycompany.com"
#                 # Create an instance of the Employee class with the provided details
#                 employee = Employee(employee_id, first_name, last_name, salary)
#                 print("Employee added successfully.")
#             elif user_input2 ==2:
#                 # employee = Employee(34, "Jane", "Markovic", 123456)
#                 # # method to update employee
#                 update_employee()
#                 # pass
#             elif user_input2 == 3:
#                 employee_id = int(input("Enter employee ID you want to delete"))
#                 delete_employee(employee_id)
#             elif user_input2 == 4:
#                 pass
#             else:
#                 print("Invalid choice. Please select a valid option.")
#
#         elif user_input == 2:
#             print("\nAttendance Management Menu:")
#             print("1. Record Attendance")
#             print("2. Display Attendance Records")
#             print("3. Back")
#             choice = input("Enter your choice (1/2/3): ")
#             if choice == '1':
#                 try:
#                     employee_id = int(input("Enter employee ID: "))
#                     date = input("Enter the date (YY-MM-DD): ")
#                     in_time = input("Enter check-in time (HH:MM): ")
#                     out_time = input("Enter check-out time (HH:MM): ")
#
#                     # Validate date, in_time, and out_time formats
#                     datetime.strptime(date, "%Y-%m-%d")
#                     datetime.strptime(in_time, "%H:%M")
#                     datetime.strptime(out_time, "%H:%M")
#
#                     # Create an instance of the Attendance class
#                     attendance = Attendance(employee_id)
#
#                     # method to record attendance
#                     attendance.record_attendance(date, in_time, out_time)
#                 except ValueError:
#                     print(
#                         "Invalid input format. Please follow the specified format for employee ID, date, in_time, and out_time.")
#                 except Exception as e:
#                     print(f"An error occurred: {e}")
#
#             elif choice == '2':
#                 employee_id = int(input("Enter employee ID: "))
#                 attendance2 = Attendance(employee_id)
#                 # method to display attendance
#                 attendance2.display_individual_attendance()
#             elif choice == '3':
#                 pass
#             else:
#                 print("Invalid choice. Please select a valid option.")
#
#         elif user_input == 3:
#             print("\nSalary Management Menu:")
#             print("1. Calculate Salary")
#             print("2. Generate Pay Slip")
#             print("3. Back")
#             choice2 = input("Enter your choice (1/2/3): ")
#             if choice2 == '1':
#                 employee_id = int(input("Enter employee ID: "))
#                 base_salary = int(input("Enter base salary"))
#                 allowances = int(input("Enter allowances"))
#                 bonuses = int(input("Enter bonuses"))
#                 deductions = int(input("Enter deductions\n"))
#                 salary = Salary(employee_id, base_salary, allowances, bonuses,deductions)
#                 salary.display_salary()
#             elif choice2 == '2':
#                 employee_id = int(input("Enter employee ID: "))
#                 base_salary = int(input("Enter base salary"))
#                 allowances = int(input("Enter allowances"))
#                 bonuses = int(input("Enter bonuses"))
#                 deductions = int(input("Enter deductions\n"))
#                 salary = Salary(employee_id, base_salary, allowances, bonuses, deductions)
#                 salary.generate_pay_slip()
#             elif choice2 == '3':
#                 pass
#             else:
#                 print("Invalid choice. Please select a valid option.")
#
#         elif user_input == 4:
#             print("Closing the application")
#             exit()
#
#
# if __name__ == "__main__":
#     main()