# True & False in Python
# In Python, every value can be evaluated as True or False

# num =0 is False and all other comes under True

# Different Data types in Python
num = -15                       # Non-zero number → True
num2 = 0                        # Zero → False
cities = ["Tirupati", "Chittoor"] # Non-empty list → True
empty_tuple = ()                # Empty tuple → False
mytuple = ("Python", "DevOps")  # Non-empty tuple → True
empty_string = ""               # Empty string → False
mystr = "VENU"                  # Non-empty string → True
empty_set = set()               # Empty set → False
myset = {"Docker", "DockerHub"} # Non-empty set → True
empty_dict = {}                 # Empty dictionary → False
mydict = {"Tool": "Ansible"}    # Non-empty dictionary → True
mydict2 = {"India": ""}         # Non-empty dictionary with empty value → True
# Check boolean value of each variable
data = [num, num2, cities, empty_tuple, mytuple, empty_string, mystr, empty_set, myset, empty_dict, mydict]

for item in data:
    # bool(item) returns True or False based.
    print(f"Value: {item}, Boolean: {bool(item)}")


# Assignment 2: While Loop

# While loop repeats until the condition becomes False
# Here we countdown from 5 to 1.

count = 5
while count:
    print(f"Countdown: {count}")
    count -= 1  # Decrease count by 1 each time
print("Lift off!")  # Printed when loop ends

# Assignment 3: For Loop

# For loop is used to iterate over a sequence like list or tuple
# Here, we print each fruit with its index number

fruits = ("Apple", "Banana", "Cherry", "Mango")

for index in range(len(fruits)):
    # index starts from 0, so we add +1 for human-readable numbering
    print(f"Fruit {index + 1}: {fruits[index]}")


Marvels = ["TonyStark", "Bruce", "Thor", "Steve", "Natasha"]
print(f"Original list: {Marvels}")

# The loop continues as long as the list is not empty (truthy)
while Marvels:
    print(f"Removing {Marvels[0]} from the list...")
    del Marvels[0]  # Delete the first element
    print(f"Updated list: {Marvels}")


# Assignment 5: Object-Oriented Programming (OOP)

# A class is for creating objects
# Objects represent attributes & methods

class Car:
    # __init__ is a special method used for initializing objects
    def __init__(self, brand, model, year):
        self.brand = brand  # Attribute 1
        self.model = model  # Attribute 2
        self.year = year    # Attribute 3
    
    # Method to return formatted car details
    def get_car_details(self):
        return f"{self.brand} {self.model}, Year: {self.year}"

# Creating two car objects with different values
Car1 = Car("Tesla", "Model S", 2022)
Car2 = Car("Toyota", "Fortuner", 2021)

# Accessing method to display car info
print(Car1.get_car_details())
print(Car2.get_car_details())
