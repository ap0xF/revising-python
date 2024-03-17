class Employee:
    def __init__(self, employee_id, first_name, last_name, salary: int, bonus: int, allowance: int):
        self.id = employee_id
        self.name = first_name + last_name
        self.benefits = salary + bonus + allowance

    def populate_get_details_results(self):
        result = {"ID": self.id, "Name": self.name, "Benefits": self.benefits}
        return result

    def get_details(self):
        return self.populate_get_details_results()
