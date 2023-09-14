# Create the parent class Personnel
class Personnel:
    def __init__(self, name, rank):
        self.name = name  # Common attribute
        self.rank = rank  # Common attribute

    def greet(self):
        return f"Hello, I am {self.name}, a {self.rank} in the US Navy."


# Child class Enlisted inheriting from Personnel
class Enlisted(Personnel):
    def __init__(self, name, rank, pay_grade):
        super().__init__(name, rank)  # Inheriting common attributes from the parent class
        self.pay_grade = pay_grade  # Unique attribute

    # Polymorphic implementation of the greet method
    def greet(self):
        return "Hi, I'm {}, a {} (Pay Grade {}) in the US Navy.".format(self.name, self.rank, self.pay_grade)


# Child class Officer inheriting from Personnel
class Officer(Personnel):
    def __init__(self, name, rank, commission_type):
        super().__init__(name, rank)  # Inheriting common attributes from the parent class
        self.commission_type = commission_type  # Unique attribute

    # Polymorphic implementation of the greet method
    def greet(self):
        return "Greetings, I'm {}, an {} ({}) in the US Navy.".format(self.name, self.rank, self.commission_type)


# Example usage:
enlisted_member = Enlisted("Lavon Harold", "Chief Petty Officer", "E-7")
officer_member = Officer("Mike Gilday", "Admiral", "Commissioned Officer")

# Polymorphism in action
print(enlisted_member.greet())  # Calls the greet method of the Enlisted class
print(officer_member.greet())   # Calls the greet method of the Officer class