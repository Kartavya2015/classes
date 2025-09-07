height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2
print("Your BMI is: ", bmi)

if bmi <= 18.5:
    print("you are under weight")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("you are over weight")
elif bmi <= 44.9:
    print("you are severely over weight")
elif bmi <= 49.9:
    print("you are obese")
else:
    print("you are severly obese")