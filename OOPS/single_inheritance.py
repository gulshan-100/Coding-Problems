# In Single Inheritance, one class (child class) inherits the properties and behaviors (methods) of another class (parent class).

class First:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Second(First):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    # Example usage
    def display_age(self):
        print(f"Age: {self.age} and Name: {self.name}")

person = Second("Alice", 30)
person.display()
person.display_age()