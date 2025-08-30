class Animal:

    def __init__(self, breed):
        print("Hello from animal")
        self.breed = breed

    def talk(self):
        print("animal is talking")

    def move(self):
        print("animal is moving")

class Dog(Animal):  #inherit
    def __init__(self,name = "unknown"):
        super(Dog, self).__init__("Dog")
        print("Hello from dog")
        self.name = name

    def set_name(self, name):
        self.name = name

    def bark(self, message):
        msg = f"My name is {self.name}, {message}"
        print(msg)

    def walk(Self):
        print("Dog can walk")


dog1 = Dog("Scooby")
dog1.talk()
print(dog1.breed)
