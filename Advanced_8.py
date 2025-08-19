#  Proxy Design Pattern
# _________________________________________________________________________________________

from abc import ABCMeta , abstractclassmethod

class Iperson(metaclass=ABCMeta):
    @abstractclassmethod
    def person_methode():
        """ Interface Methode """


class Person(Iperson):

    def person_methode(self):
        print("I am Person !")

class ProxyPerson(Iperson):

    def __init__(self):
        self.person = Person()

    def person_methode(self):
        print("I am Proxy Functionality !")
        self.person.person_methode()

P1 = Person()
P1.person_methode()

P2 = ProxyPerson()
P2.person_methode()
