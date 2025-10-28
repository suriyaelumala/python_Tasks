# Classes and Objects in Python
# This demonstrates creating classes, objects, and methods.

# Define a class
class Car:
    # Constructor (initializes object)
    def __init__(self, brand, model):
        self.brand = brand  # Instance variable
        self.model = model
    
    # Method
    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Create objects (instances of the class)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Call methods
car1.display_info()  # Outputs: Car: Toyota Corolla
car2.display_info()  # Outputs: Car: Honda Civic