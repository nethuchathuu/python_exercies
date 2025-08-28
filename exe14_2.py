class Dog:
    name =""
    color = ""

    def set_name(self,name):
        self.name = name

    def bark(self,message):
        msg = f"woof woof my name is {self.name}, {message}"
        print(msg)

dog1 = Dog()
dog1.set_name("tommy")

dog1.bark("hello") 