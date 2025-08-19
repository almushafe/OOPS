# Encapsulation 

# 1 -
# ________________________________________________________________________________________________________________
class Person:
  def __init__(self,name,age,gender):
    self.__name = name
    self.__age =age
    self.__gender = gender
    
  @property
  def Name(self):
    return self.__name
  
  @Name.setter
  def Name(self,value):
    # if value > 0:
    # if value == "Zaid":
      self.__name = "Default Name"
    else:
      self.__name =  value 
    

P1 = Person("Aslam",20,"m")
print(P1.Name)

P1.Name = "Zaid"
print(P1.Name)


# 2 -
# ________________________________________________________________________________________________________________



class Person:
  def __init__(self,name,age,gender):
    self.__name = name
    self.__age =age
    self.__gender = gender
    
  @property
  def Name(self):
    return self.__name
  
  @Name.setter
  def Name(self,value):
    self.__name =  value 
  
  @staticmethod
  def mymethode():
    print("Helow World !")
    
Person.mymethode()
P1 = Person("Aslam",20,"m")
print(P1.Name)

P1.mymethode()

P1.Name = "Zaid"
print(P1.Name)
