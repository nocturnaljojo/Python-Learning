# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/height**2)
if bmi <18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>35:
    print(f"Your BMI is {bmi}, you are clinically obese.")

    
# Example Input
# weight = 85
# height = 1.75
# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325
# Your BMI is 28, you are slightly overweight.
