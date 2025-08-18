# 1
# _________________________________________________________________________________________________________________
def logged(function):
    def wraper(*args,**kwargs):
        value = function(*args,**kwargs)
        with open('login.txt','a+') as f :
            fname = function.__name__
            print(f.write(f"{fname} returnd value {value}"))
            f.write(f"{fname} returnd value {value}")
            return value
    return wraper

@logged
def add(x,y):
    return x + y

print(add(20,10))


# 2
# _____________________________________________________________________________________________________________
def mydecorater(func):
  
  def wraper(*args, **kwargs):
    kvalu =  func(*args,**kwargs)
    print(f"Aceept")
    return kvalu
    
  return wraper
  
@mydecorater
def Hello_world(per):
  print("i")
  return f"Hello World ! {per}"
# mydecorater(Hello_world)()
print(Hello_world('per'))
# mydecorater()


#  3 
# ____________________________________________________________________________________________________________________________

import time 

def timed(func):
  def wraper(*args,**kwargs):
    before = time.time()
    value = func(*args,**kwargs)
    after = time.time()
    fname = func.__name__
    print(f"{fname} took {after - before} second to execute !")
    return value
    
  return wraper
  
@timed
def myfunction(x):
  result = 1 
  for i in range(x):
    result *= i 
    return result
    
myfunction(1000)
