import math
x=float(input('Enter x coordinate value : '))
y0=float(input('Enter the initial position y coordinate : '))
angle=float(input('Enter angle value made with x coordinate : '))
g=9.8
v=30*(18/5)
result=(x*math.tan(angle))-((g*math.pow(x,2))/(2*math.pow(v,2)*math.pow(math.cos(angle),2)))+y0

print("result : "+str(result))



