# Create the parent class Vehicle
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand  # Common attribute for all vehicles
        self.year = year  # Common attribute for all vehicles

# Define the child class Car inheriting brand and year from Vehicle
class Car(Vehicle):
    def __init__(self, brand, year, model, color):
        self.model = model  # Unique attribute for cars
        self.color = color  # Unique attribute for cars

# Define the child class Bicycle inheriting brand and year from Vehicle
class Bicycle(Vehicle):
    def __init__(self, brand, year, type, gears):
        self.type = type  # Unique attribute for bicycles
        self.gears = gears  # Unique attribute for bicycles