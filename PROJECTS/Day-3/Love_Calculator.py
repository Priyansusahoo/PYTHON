# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_case_n1 = name1.lower()
lower_case_n2 = name2.lower()

# TRUE for lower_case_n1 & lower_case_n2
T1 = lower_case_n1.count("t")
T2 = lower_case_n2.count("t")

R1 = lower_case_n1.count("r")
R2 = lower_case_n2.count("r")

U1 = lower_case_n1.count("u")
U2 = lower_case_n2.count("u")

E1 = lower_case_n1.count("e")
E2 = lower_case_n2.count("e")

S1 = (T1+T2) + (R1+R2) + (U1+U2) + (E1+E2)

# LOVE for lower_case_n1 & lower_case_n2
L1 = lower_case_n1.count("l")
L2 = lower_case_n2.count("l")

O1 = lower_case_n1.count("o")
O2 = lower_case_n2.count("o")

V1 = lower_case_n1.count("v")
V2 = lower_case_n2.count("v")

E1 = lower_case_n1.count("e")
E2 = lower_case_n2.count("e")

S2 = (L1+L2) + (O1+O2) + (V1+V2) + (E1+E2)

Test_Percent = str(S1) + str(S2)
percent = int(Test_Percent)

if (percent <= 10) or (percent >= 90):
    print(f"Your score is {percent}, you go together like coke and mentos.")
elif (percent >=40 and percent <= 50):
    print(f"Your score is {percent}, you are alright together.")
else:
    print(f"Your score is {percent}.") 


###############################################################
# tutorial solution


combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = str(true) + str(love)

score = int(love_score)

if (score <= 10) or (score >= 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >=40 and score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.") 



