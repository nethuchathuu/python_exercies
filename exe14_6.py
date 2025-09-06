class Animal:
    def __init__(self, breed):
        print("Hello from animal")
        self.breed = breed

    def talk(self):
        print("animal is talking")

    def move(self):
        print("animal can move")

class Dog(Animal):
    def __init__(self, name = "unknown"):
        super(Dog, self).__init__("Dog")
        print("Hello from dog")
        self.name = name

    def set_name(self, name):
        self.name = name

    def talk(self):
        super(Dog, self).talk()
        print("Dog is talking")

    def bark(self, message):
        msg = f"woof woof, my name is {self.name}, {message}"
        print(msg)

dog1 = Dog("Scooby")
dog1.talk()