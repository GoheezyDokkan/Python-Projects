from abc import ABC, abstractmethod

# Define an abstract class representing a US Navy Ship
class USNavyShip(ABC):
    def __init__(self, name, classification, captain):
        self.name = name
        self.classification = classification
        self.captain = captain

    # Regular method to display ship information
    def display_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Classification: {self.classification}")
        print(f"Captain: {self.captain}")

    # Abstract method to be implemented by child classes
    @abstractmethod
    def mission(self):
        pass

# Create a child class that implements the abstract method
class AircraftCarrier(USNavyShip):
    def __init__(self, name, captain):
        # Call the parent class constructor with attribute values
        USNavyShip.__init__(self, name, "Aircraft Carrier", captain)

    # Implementing the abstract method
    def mission(self):
        print(f"{self.name} is conducting air operations in support of naval forces.")

if __name__ == "__main__":
    # Create an object of the child class
    nimitz = AircraftCarrier("USS Nimitz", "Captain Smith")

    # Call regular method from the parent class
    nimitz.display_info()

    # Call the abstract method from the child class
    nimitz.mission()
