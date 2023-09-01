# uppgift 1 
"""
    Multi 
    line 
    comment 
"""


# uppgift 2 
print(400 + 10)


# uppgift 3 
name = input("enter your name :")
age = int(input("how old are you ?:"))

print("Welcome Mr.%s !" %(name) if age > 18 else "Welcome %s !" %(name))


# uppgift 4
first_number = int(input("enter your first number :"))
second_number = int(input("enter your second number :"))
print(first_number * second_number)


# uppgift 5
weight = int(input("enter your weight :"))
height = int(input("enter your height :"))

print("your BMI is : %s" %(weight / (height / 100) ** 2))


# uppgift 6 
age = int(input("enter your age :"))
print("You lived - %s weeks" %(age * 52))


# uppgift 7
weight = int(input("enter your weight :"))
print("Your weight in lbs : %s" %(weight * 2.2))
