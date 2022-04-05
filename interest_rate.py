import math
from typing import final
amount=float(input('Enter the amount of investment : '))
rateOfInterest=float(input('Enter the rate of Interest : '))
numbersOfYears=float(input('Enter numbers of years for investment : '))
res=1+(rateOfInterest/100)
finalAmount=amount*math.pow(res,numbersOfYears)

print("Amount got after {0} years of amount {1} at rate {2} is {3}: ".format(numbersOfYears,amount,rateOfInterest,finalAmount))

