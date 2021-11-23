# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
s_BMI = weight/height ** 2
BMI = round((s_BMI),2)

if BMI < 18.5:
  print(f"Your BMI is {BMI} & you are underweight")
elif BMI < 25:
  print(f"Your BMI is {BMI} and your have normal weight")
elif BMI < 30:
  print(f"Your BMI is {BMI} & you are overweight")
elif BMI < 35:
  print(f"Your BMI is {BMI} and you are Obese")
else:
  print(f"Your BMI is {BMI} and you are clinically Obese")