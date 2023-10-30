class Attendance:
    def __init__(self):
        self.attendance_records = {}

    def check_existing_ids(self, employee_id):
        try:
            with open("existing_ids.txt", 'r') as file:
                existing_ids = set(map(int, file.read().split()))
                return employee_id in existing_ids
        except FileNotFoundError:
            return False

    def record_attendance(self, employee_id, date, in_time, out_time):
        # Check if the employee ID exists
        if not self.check_existing_ids(employee_id):
            print(f"Employee ID {employee_id} does not exist. Attendance not recorded.")
            return

        if employee_id not in self.attendance_records:
            self.attendance_records[employee_id] = []

        self.attendance_records[employee_id].append({
            'date': date,
            'in_time': in_time,
            'out_time': out_time
        })

    def get_employee_attendance(self, employee_id):
        if employee_id in self.attendance_records:
            return self.attendance_records[employee_id]
        else:
            return []

    # def get_employee_attendance(self, employee_id):
    #     if employee_id in self.attendance_records:
    #         attendance_data = self.attendance_records[employee_id]
    #         if attendance_data:
    #             for entry in attendance_data:
    #                 print(entry)
    #         else:
    #             print(f"No attendance records found for employee {employee_id}")
    #     else:
    #         print(f"No attendance records found for employee {employee_id}")

    def get_all_employees_attendance(self):
        return self.attendance_records

    def calculate_working_hours(self, employee_id, start_date, end_date):
        if employee_id in self.attendance_records:
            total_working_hours = 0
            for record in self.attendance_records[employee_id]:
                if start_date <= record['date'] <= end_date:
                    in_time = record['in_time']
                    out_time = record['out_time']
                    in_time = int(in_time.split(":")[0]) + int(in_time.split(":")[1]) / 60
                    out_time = int(out_time.split(":")[0]) + int(out_time.split(":")[1]) / 60
                    total_working_hours += (out_time - in_time)
            return total_working_hours
        else:
            return 0
