class InvalidNameException(Exception):
    def __init__(self, error):
        super(InvalidNameException, self).__init__(error)
        self.error_code = 10

class InvalidAgeException(Exception):
    def __init__(self, error):
        super(InvalidAgeException, self).__init__(error)
        self.error_code = 5

class Person:
    def __init__(self, name, age):
        super().__init__()

        self.name = name
        self.age = age

    @staticmethod
    def get_person(name, age):
        if not name:
            raise InvalidNameException("Invalid name")
        if age < 0 or age >= 120:
            raise InvalidAgeException("Invalid age")

        return Person(name, age)


try:
    person = Person.get_person("", -22)

    print(person)

except (InvalidNameException, InvalidAgeException) as e:
    print("error found", e)