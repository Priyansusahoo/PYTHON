print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  age = int(input("What is your Age? "))
  if age < 12:
    print("Child ticket are 5$.")
    bill = 5
  elif age <= 18:
    print("Youth ticket are 7$.")
    bill = 7
  else:
    print("Adult ticket are 12$.")
    bill = 12

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    #Add $3
    bill += 3 
    print(f"Your final ticket price is = ${bill}")
else:
  print("GETLOST! At least built your height to 120cm")