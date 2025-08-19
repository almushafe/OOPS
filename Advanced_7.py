# Factory Design Pattern
# ___________________________________________________________________-
from abc import ABCMeta, abstractclassmethod
class IPerson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_method():
        """ Interface Method"""
class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"
    
    def person_method(self):
        print("I am a student ")

class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher ")


class PersonFactory:
    @staticmethod
    def bulid_person(personType):
        if personType == "Student":
            return Student()
        if personType == "Teacher":
            return Teacher()
        print("Invalid Type ")
        return -1
    

if __name__ == "__main__":
    choice = input("What Type  of Person do you want to create ? \n\t: ")
    Person = PersonFactory.bulid_person(choice)
    Person.person_method()


# s1 = Student()
# s1.person_method()

# t1 = Teacher()
# t1.person_method()


