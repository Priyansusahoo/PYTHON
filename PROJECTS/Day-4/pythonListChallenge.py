# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_names = random.choice(names)
print(f"{random_names} is going to buy the meal today")