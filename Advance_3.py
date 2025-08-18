# 1 .
# ___________________________________________________________________
def myfunction(x):
  for x in range(x):
    yield x**3
    
value = myfunction(90000)

# for i in myfunction(10):
#   print(i)
  
print(next(value))
print(next(value))
print(next(value))
print(next(value))
print(next(value))

# 2 .
# ________________________________________________________________________


import sys

def myfunction(x):
  for x in range(x):
    yield x**3
    
value = myfunction(90000)
print(sys.getsizeof(value))

for i in myfunction(10):
  print(i)
  
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))
# print(next(value))

# 3 .
# ____________________________________________________________________________________


def infinite_seq():
  result =  1 
  while True:
    yield result
    result *= 5
    

values = infinite_seq()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

for i in values:
  print(i)

