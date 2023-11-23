class Employee:

    def __init__(self, name, id, salary, department):

        self.name = name
        self.id = id
        self.salary = salary
        self.department = department


    def assign_department(self, department):

        self.department = department


    def print_employee_details(self):

        print(f"{self.name}, {self.id}, {self.salary}, {self.department}\n")


    def calculate_emp_salary(self, time):

        self.plus_time = time-50
        if self.plus_time>0 :
            self.salary = self.salary + (self.plus_time*(self.salary/50))
            print(f"{self.name}, {self.id}, {int(self.salary)}, {self.department}\n")
        else:
            print(f"{self.name}, {self.id}, {int(self.salary)}, {self.department}\n")



emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()

print("-----------------------------------")

emp1.assign_department("SALES")
emp2.assign_department("OPERATIONS")
emp3.assign_department("ACCOUNTING")
emp4.assign_department("RESEARCH")

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()

print("-----------------------------------")

emp1.calculate_emp_salary(69)
emp2.calculate_emp_salary(44)
emp3.calculate_emp_salary(72)
emp4.calculate_emp_salary(50)