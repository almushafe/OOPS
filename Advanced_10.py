# Composite Design Pattern
# ____________________________________________________________
from abc import ABCMeta ,abstractclassmethod ,abstractmethod ,abstractstaticmethod

class IDeparment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self,empolyees):
        """ Implement in Child class"""

    @abstractstaticmethod
    def print_deparment():
        """ implement in  child class"""


class Acountaing(IDeparment):

    def __init__(self, empolyees):
        self.empolyees = empolyees

    def print_deparment(self):
        print(f"Acountaing Deparment  : {self.empolyees}")

class Development(IDeparment):

    def __init__(self, empolyees):
        self.empolyees = empolyees

    def print_deparment(self):
        print(f"Development  Deparment  : {self.empolyees}")

class ParentDeparment(IDeparment):

    def __init__(self, empolyees):
        self.empolyees = empolyees
        self.base_employees = empolyees
        self.sub_depts = []

    def add(self,dept):
        self.sub_depts.append(dept)
        self.empolyees += dept.empolyees

    def print_deparment(self):
        print("Parent Development")
        print(f"Print Deparment Base Employees : {self.base_employees}")

        for dept in self.sub_depts:
            dept.print_deparment()
        
        print(f"Total Number of Employees : {self.empolyees}")


dept1 = Acountaing(200)
dept2 = Development(170)

Parent_dept = ParentDeparment(30)
Parent_dept.add(dept1)
Parent_dept.add(dept2)

Parent_dept.print_deparment()
