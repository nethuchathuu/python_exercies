class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 25
        self._city = "Kandy"

    def set_age(self, age):
        self.__age = age

    def _calculate_age(self):
        return 30

    def get_age(self):
        return self.__age

    def sleep(self):
        print("Sleeping ", self.name)

class Student(Person):
    def __init__(self, name):
        super(Student, self).__init__(name)

    def print_age(self):
        print(self.__age)

    def _calculate_age(self):
        age = super(Student, self)._calculate_age()
        return age -5
    

    def print_city(self):
        print(self._city)





person1 = Student("Nethu")
person1.sleep()
person1.set_age(30)
person1.print_city()


#access modifiers
  #private: __variableName/functionName
  #protected: _variableName/functionName
  #public : variableName/functionName