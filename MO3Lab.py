# Lynn Prout - SDEV220 1st 8 weeks Spring 2024
# M03 Lab - Case Study: Lists, Functions, and Classes

class Vehicle:  # Super (Parent) class
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):  # Child Class
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self): # Print descriptions for user entered data 
        print("\nVehicle Information:")
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

         # user input code
vehicle_type = input("Enter the type of vehicle (car, truck, etc..): ")
year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")
doors = input("Enter the number of doors (2 or 4): ")
roof = input("Enter the type of roof (solid or sun roof): ")

# Creation of an Automobile object with input entered by the user.
automobile = Automobile(vehicle_type, year, make, model, doors, roof)

# This displays the user entered information
automobile.display_info()

