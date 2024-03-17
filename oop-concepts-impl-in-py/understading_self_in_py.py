class Employee:
    def __init__(self, first_name, last_name):
        self.pahilo_naam = first_name
        self.doshro_naam = last_name
        self.message = 'Sawagat Chha '
        print(self)

    def get_full_name(self):
        return self.message + self.pahilo_naam + " " + self.doshro_naam


if __name__ == "__main__":
    emp1 = Employee("Aadit", "Panta")

if __name__ == "__main__":
    emp2 = Employee("Aadit", "Panta")
