# In multiple inheritance, one class (child class) inherits the properties and behaviors (methods) from more than one class (parent classes).

class First:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")

class Second():
    def __init__(self, age):
        self.age = age
    
    def display_age(self):
        print(f"Age: {self.age}")

class Third(First, Second):
    def __init__(self, name, age, city):
        First.__init__(self, name)
        Second.__init__(self, age)
        self.city = city
    
    def display_city(self):
        print(f"City: {self.city}")

    def display_all(self):
        self.display()
        self.display_age()
        self.display_city()

# Example usage
person = Third("Bob", 25, "New York")
person.display_all()

