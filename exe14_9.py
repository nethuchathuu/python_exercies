class Person :
    types = ["student", "teacher", "librarian"]  #class atribuites


    def __init__(self, name = "unknown"):
        print("Person is created")
        self.name = name

    def print_name(self):
        print("Name: ", self.name)


    @classmethod  #decoraters
    def get_types(cls):
        return cls.types
    

    @staticmethod
    def get_person():
        return Person()


person1 = Person("nethu")

p = Person.get_person()
print(p.name)