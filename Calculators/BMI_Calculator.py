weight = float(input ("What is your weight (in kg) : "))
height = float(input ("What is your height (in m) : "))

bmi = weight / (height ** 2)

print(f"Yoy BMI is {bmi}")
if bmi < 18.5 :
    print("You are Underweight.")
elif bmi < 25 :
    print("You are normal weight")
else :
    print("You are Overweight")