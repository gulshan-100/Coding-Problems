# Example of Hierarchical Inheritance in Python

class First:
    def __init__(self, name):
        self.name = name

class Second(First):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Third(First):
    def __init__(self, name, age, city):
        super().__init__(name)
        self.age = age
        self.city = city

# Creating instances
first_instance = First("Alice")
second_instance = Second("Bob", 30)
third_instance = Third("Charlie", 25, "New York")

# display the result 
print(f"First Instance: Name = {first_instance.name}")
print(f"Second Instance: Name = {second_instance.name}, Age = {second_instance.age}")
print(f"Third Instance: Name = {third_instance.name}, Age = {third_instance.age}, City = {third_instance.city}")