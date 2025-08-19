# 1 -
# ________________________________________________________________________________________________________________
def myfunction(*args,**kwargs):
  print(args[0])
  print(args[1])
  print(args[2])
  print(args[3])
  print(kwargs['KEYONE'])
  print(kwargs['KEYTOW'])
  
myfunction('Aslam',3,True,'wow',KEYONE='Yar',KEYTOW=23)

# 2 -
# ________________________________________________________________________________________________________________

import sys
filename = sys.argv[1]
massge = sys.argv[2]

with open(filename,'w+') as f:
    f.write(massge)

# 3 -
# ________________________________________________________________________________________________________________

import sys
import getopt

filename = "text.txt"
massge = "print"

opts,args = getopt.getopt(sys.argv[1:], "f:m:" ,['filname','massge'])
for opt,arg in opts:
    if opt == '-f':
        filename = arg
    if opt == "-m":
        massge = args

with open(filename,'w+') as f :
    f.write(massge)

# print(opts)
# print(args)
