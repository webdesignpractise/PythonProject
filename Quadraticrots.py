import math
from re import A
a=int(input('Enter the value for "a" : '))
b=int(input('Enter the value for "b" : '))
c=int(input('Enter the value for "c" : '))

dis=b**2 - 4*a*c

if dis == 0 :
    print("Root are real ans equal and value is {0}".format(-1*b/(2*a)))
elif dis > 0 :
    dis=math.sqrt(dis)
    print("Roots are real and distinct")
    print("Root I is {0}".format(-1*(b+dis)/(2*a)))
    print("Root II is {0}".format(-1*(b-dis)/(2*a)))
else:
    print("Roots are imaginary")
    dis*=-1
    dis=math.sqrt(dis)
    print("Root I is {0}+{1} i".format(-1*b/(2*a),dis/(2*a)))
    print("Root II is {0}+{1} i".format(-1*b/(2*a),-dis/(2*a)))

