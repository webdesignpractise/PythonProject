import math
def factorialThroughIterator(num):
    if num < 0 :
        return -1
    result=1
    for i in range(2,num+1):
        result=result*i;
    return result;

def factorialRecursion(num):
    if num < 0 :
        return -1
    if num==0 or num==1:
        return 1
    return num*factorialRecursion(num-1)

def factorialMath(num):
    if num < 0 :
        return -1
    return math.factorial(num)

num=int(input('Enter a number : '))

print(factorialThroughIterator(num))
print(factorialRecursion(num))
print(factorialMath(num))