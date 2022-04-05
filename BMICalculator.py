weight=float(input('Enter your weight in Killogram : '))
height=float(input('Enter your height in meter : '))

BMI=weight/(height*height)
print("BMI for the given data is : "+str(BMI))

if BMI <= 18.5 :
    print("Under Weight")
elif BMI > 18.5 and BMI <=24.9:
    print("Normal Weight")
elif BMI >=25.0 and BMI < 29.9:
    print("Over Weight")
elif BMI >=30.0 and BMI < 34.9:
    print("Obesity class I")
elif BMI >=35.5 and BMI <39.9:
    print("Obesity class II")
elif BMI >= 40.0 :
    print("Obesity class III")
