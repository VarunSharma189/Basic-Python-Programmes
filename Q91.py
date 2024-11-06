# WAP in python to demonstrate the concept of Encapsulation

class Car:
    def __init__(self, make, model, year):
        self._make = make       # Private attribute by convention
        self._model = model
        self._year = year

    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")

    def set_year(self, year):
        if year > 1885:  
            self._year = year
        else:
            print("Invalid year")

# Example usage
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()          

car1.set_year(2022)          
car1.display_info()          

car1.set_year(1800)  
print("THIS PROGRAM IS WRITTEN BY VARUN SHARMA ERP :- 0221BCA136")        