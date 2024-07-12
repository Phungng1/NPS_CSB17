# Bai 1
fname = input("First name: ")
lname = input("Last name: ")
print(f"your full name is {fname} {lname}")
# Bai 2
name = input("Your input: ")
name2 = name.upper()
print(f"Capitalized: {name2}")

name.upper()
# Bai 3
num = float(input("Input a number: "))
import math
num2 = num*num
print(f"Squared input: {math.sqrt(num2)}")
# Bai 4
import turtle
t = turtle.Turtle()
radius = float(input("Input circle's radius: "))
t.circle(radius*2)
