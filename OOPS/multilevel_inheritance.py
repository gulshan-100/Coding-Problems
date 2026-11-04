class First:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")

class Second(First):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"Age: {self.age}")

class Third(Second):
    def __init__(self, name, age, city):
        super().__init__(name, age)
        self.city = city

    def display_city(self):
        print(f"City: {self.city}")

    def display_all(self):
        self.display()
        self.display_age()
        self.display_city()

# Example usage
person = Third("Charlie", 28, "Los Angeles")
person.display_all()

