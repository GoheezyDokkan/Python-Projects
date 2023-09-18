import time

class USNavyShip:
    def __init__(self, name, classification, captain):
        # Public attributes
        self.name = name
        self.classification = classification

        # Protected attribute (prefixed with underscore)
        self._captain = captain

        # Private attribute (prefixed with double underscore)
        self.__is_sailing = False

    # Public method to start sailing
    def start_sailing(self):
        if not self.__is_sailing:
            print(f"{self.name} is setting sail!")
            self.__is_sailing = True
        else:
            print(f"{self.name} is already sailing.")

    # Public method to stop sailing
    def stop_sailing(self):
        if self.__is_sailing:
            print(f"{self.name} is stopping its engines.")
            self.__is_sailing = False
        else:
            print(f"{self.name} is already stopped.")

    # Protected method (prefixed with underscore)
    def _change_captain(self, new_captain):
        print(f"Changing captain from {self._captain} to {new_captain}")
        self._captain = new_captain

    # Public method to display ship information
    def display_info(self):
        print(f"Ship Name: {self.name}")
        print(f"Classification: {self.classification}")
        print(f"Captain: {self._captain}")
        print(f"Sailing Status: {'Sailing' if self.__is_sailing else 'Stopped'}")


if __name__ == "__main__":
    # Create an object of the USNavyShip class
    ship1 = USNavyShip("USS Nimitz", "Aircraft Carrier", "Captain Smith")

    # Calling public methods
    ship1.start_sailing()
    ship1.stop_sailing()
    ship1.start_sailing()

    # Calling the protected method
    time.sleep(1)
    ship1._change_captain("Captain Johnson")

    # Display ship information after changing captain
    time.sleep(1)
    ship1.display_info()
