# WAP in python to demonstrate the concept of Inheritance

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)  # Call the base class constructor
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()  # Call the base class display_info method
        print(f"Fuel type: {self.fuel_type}")

# Example usage
car1 = Car("Toyota", "Corolla", 2020, "Gasoline")
car1.display_info()
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")