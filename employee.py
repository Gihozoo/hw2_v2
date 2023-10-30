import os


class Employee:
    def __init__(self, employee_id, first_name, last_name, salary):
        # Check if the employee ID already exists in the file
        if self.check_existing_ids(employee_id):
            print(f"Cannot create a new employee. Employee ID {employee_id} already exists.")
            return  # Exit the constructor

        # Generate a random employee id
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        # Create an email address based on first name and last name
        self.__email = self.__first_name + "." + self.__last_name + "@mycompany.com"
        self._salary = salary

        # Save the employee's information to a file
        self.save_all_to_file("employee_records.txt")
        # Save the employee's information to a file
        self.save_to_file()
        # Add the ID to the file of existing IDs
        self.add_existing_id(employee_id)

    def check_existing_ids(self, employee_id):
        try:
            with open("existing_ids.txt", 'r') as file:
                existing_ids = set(map(int, file.read().split()))
                return employee_id in existing_ids
        except FileNotFoundError:
            return False

    def add_existing_id(self, employee_id):
        with open("existing_ids.txt", 'a') as file:
            file.write(f"{employee_id}\n")

    # Method to set the salary of an employee
    def set_salary(self, amount):
        self._salary = amount
        return self._salary

    # Method to display information of the Employee
    def __str__(self):
        return (f" Employee ID : {self.__employee_id}\n"
                f" First name : {self.__first_name}\n"
                f" Last name : {self.__last_name}\n"
                f" email : {self.__email}\n\n\n")

    def save_to_file(self):
        folder_path = "employee_records"
        os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
        filename = os.path.join(folder_path, f"employee_{self.__employee_id}.txt")
        try:
            with open(filename, 'w') as file:
                file.write(str(self))
        except FileNotFoundError:
            print(f"Error: The file '{filename}' could not be created.")

    def save_all_to_file(self, file_name):
        try:
            with open(file_name, 'a') as file:
                file.write(str(self))
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
