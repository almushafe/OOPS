class vector:
  def __init__(self, x , y ):
    self.x = x
    self.y = y
    
  def __add__(self,other):
    
    return vector(self.x + other.x,  self.y + other.y)
    
  def __sub__(self,other):
    return vector(self.x - other.x , self.y - other.y)
    
  def __mul__(self,other):
    return vector(self.x * other.x , self.y * other.y)
    
  def __truediv__(self,other):
    return vector(self.x / other.x , self.y / other.y)
    
  def __repr__(self):
    return f"X: {self.x}, Y: {self.y}"
    
  def __call__(self):
    print(f"call : {self.x}")
    
  def __len__(self):
    return 10
    
  def __repr__(self):
    return f"X: {self.x}, Y: {self.y}"
    

v1 = vector(20,23)
v2 = vector(23,20)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2
v6 = v1 / v2

print("Adition \n")
print(v3)
print(v3.x)
print(v3.y)
print("\n")

print("Subbtraction \n")
print(v4)
print(v4.y)
print(v4.y)
print("\n")

print("Multiplay \n")
print(v5)
print(v5.y)
print(v5.y)
print("\n")

print("Dvide \n")
print(v6)
print(v6.y)
print(v6.y)

print("\n")

v3()


