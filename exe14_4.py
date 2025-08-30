class Dog:

    # constructor
    def __init__(self, name = "Unknown"):   #constatnt method
        self.name = name

    def set_name(self, name):
        self.name = name

    def bark(self, message):
        msg = f"My name is {self.name}, {message}"
        print(msg)

    def walk(self):
        print("i can walk")

dog1 = Dog("Scooby")
dog1.bark("Heyyy")

dog2 = Dog()
dog2.bark("hello")