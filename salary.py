from employee import Employee


class Salary:
    tax_rate = 0.3

    def __init__(self, employee_id, base_salary, allowances=0, bonuses=0, deductions=0):

        # Check if the employee ID exists
        if not self.check_existing_ids(employee_id):
            print(f"Employee ID {employee_id} does not exist. Attendance not recorded.")
            return

        self.employee_id = employee_id
        self.base_salary = float(base_salary)
        self.allowances = float(allowances)
        self.bonuses = float(bonuses)
        self.deductions = float(deductions)

    def check_existing_ids(self, employee_id):
        try:
            with open("existing_ids.txt", 'r') as file:
                existing_ids = set(map(int, file.read().split()))
                return employee_id in existing_ids
        except FileNotFoundError:
            return False

    # Method to set the salary of an employee
    def set_salary(self, amount):
        self.base_salary = amount

    def set_allowances(self, amount):
        self.allowances = amount

    def set_bonuses(self, amount):
        self.bonuses = amount

    def set_deductions(self, amount):
        self.deductions = amount

    def calculate_monthly_salary(self):
        if not self.check_existing_ids(self.employee_id):
            return {
                "message": f"Employee ID {self.employee_id} does not exist."
            }

        taxable_income = self.base_salary + self.bonuses - self.deductions
        tax_amount = taxable_income * self.tax_rate
        net_pay = self.base_salary + self.allowances + self.bonuses - tax_amount - self.deductions

        return {
            "Base Salary": self.base_salary,
            "Allowances": self.allowances,
            "Bonuses": self.bonuses,
            "Deductions": self.deductions,
            "Tax Amount": tax_amount,
            "Net Pay": net_pay,
        }

    def display_salary(self):
        salary_details = self.calculate_monthly_salary()
        print(f"Salary details for Employee {self.employee_id}:")
        for component, amount in salary_details.items():
            print(f"{component}: {amount:.2f}")

    def generate_pay_slip(self):
        salary_details = self.calculate_monthly_salary()
        if "message" in salary_details:
            print(salary_details["message"])
        else:
            pay_slip_filename = f"{self.employee_id}.txt"
            with open(pay_slip_filename, 'w') as file:
                file.write(f"Pay Slip for Employee {self.employee_id}\n")
                file.write("=" * 30 + "\n")
                for component, amount in salary_details.items():
                    file.write(f"{component}: {amount:.2f}\n")
                file.write("=" * 30 + "\n")


employee_1_salary = Salary(1, 100000, 0, 10000, 500)
employee_1_salary.calculate_monthly_salary()
