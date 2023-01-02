import math
x=int(input('x sonini kirit: '))
y=int(input('y sonini kirit: '))
z=int(input('z sonini kirit: '))
if x+y>y+z:
    print(x,y)
elif x+z>y+z:
    print(x,z)
else: print(y,z)

