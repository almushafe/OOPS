# Type Hinting
# 1 -
# ________________________________________________________________________________________________________________
def myfunction(myprameter: int) -> int:
    return myprameter + 10
    
def otherfunction(otherpremeter:str):
  print(otherpremeter)
    
otherfunction(myfunction(45))

# 2 -
# ________________________________________________________________________________________________________________

def myfunction(myprameter: int) -> int:
    return myprameter + 10
    
def otherfunction(otherpremeter:str):
  print(otherpremeter)
    
otherfunction(myfunction(45))

def dosth(param: list[int])
