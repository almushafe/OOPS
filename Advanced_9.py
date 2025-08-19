# Singleton Design Pattern 
# __________________________________________________________________________

from abc import ABCMeta ,abstractclassmethod

class Iperson(metaclass=ABCMeta):

    @abstractclassmethod
    def print_data(self):
        """ implement in child class """

class PersonSingleton(Iperson):

    __instance = None

    @staticmethod
    def get_istance():
        if PersonSingleton.__instance == None :
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance
    
    def __init__(self,name,age):
        if PersonSingleton.__instance != None :
            raise Exception("Singleton Cannot be instandiated more than once !")
        else:        
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

    @staticmethod
    def print_data():
        print(f"Name : {PersonSingleton.__instance.name},  Age : {PersonSingleton.__instance.age}")

p = PersonSingleton("Aslam",20)
print(p)
p.print_data()

g = PersonSingleton("ZAID",17)
print(g)
g.get_istance()
