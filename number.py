# 1. Write a program that generates and prints 50 random integers, each between 3 and 6.
from random import randint

x = randint(3, 6)
print(x)

# 2. Write a program that generates a random number, x, between 1 and 50, a random number y
# between 2 and 5, and computes x^y.
x = randint(1, 50)
y = randint(2, 5)
print(f'x = {x} and y = {y} and x^y is ', x**y)

# 3. Write a program that generates a random number between 1 and 10 and prints your name
# that many times.
z = randint(1, 10)
print(z)
for i in range(z):
    print(i+1, 'Ken')

# 4. Write a program that generates a random decimal number between 1 and 10 with two decimal
# places of accuracy. Examples are 1.23, 3.45, 9.80, and 5.00.
import random

random_number = random.uniform(1, 10)
formatted_number = "{:.2f}".format(random_number)
print(formatted_number)

# 5. Write a program that generates 50 random numbers such that the first number is between 1
# and 2, the second is between 1 and 3, the third is between 1 and 4, . . . , and the last is between
# 1 and 51.
import random

for i in range(1, 51):
    random_number = random.randint(1, i)
    print(random_number)

# 6. Write a program that asks the user to enter two numbers, x and y, and computes |x−y| / x+y.
x = float(input("Enter the first number (x): "))
y = float(input("Enter the second number (y): "))

result = abs(x - y) / (x + y)
print("The result of |x-y| / (x+y) is:", result)

# 7. Write a program that asks the user to enter an angle between −180◦
# and 180◦. Using an expression with the modulo operator, convert the angle to its equivalent between 0◦ and 360◦.
angle = int(input("Enter an angle between -180 and 180 degrees: "))

# Convert the angle to the range 0 to 360 degrees
normalized_angle = (angle + 360) % 360

print("The equivalent angle between 0 and 360 degrees is:", normalized_angle)

# 8. Write a program that asks the user for a number of seconds and prints out how many minutes
# and seconds that is. For instance, 200 seconds is 3 minutes and 20 seconds. [Hint: Use the //
# operator to get minutes and the % operator to get seconds.]
time = int(input('Enter seconds: '))
minutes = time // 60
seconds = time % 60
print(f'The time is {minutes} minutes and {seconds} seconds')

# 9. Write a program that asks the user for an hour between 1 and 12 and for how many hours in
# the future they want to go. Print out what the hour will be that many hours into the future.
current_hour = int(input("Enter the current hour (1-12): "))
hours_ahead = int(input("Enter the number of hours ahead: "))

future_hour = (current_hour + hours_ahead - 1) % 12 + 1

print("The hour", hours_ahead, "hours into the future will be:", future_hour)

# 10. (a) One way to find out the last digit of a number is to mod the number by 10. Write a
# program that asks the user to enter a power. Then find the last digit of 2 raised to that
# power.
power = int(input("Enter a power: "))

last_digit = 2**power % 10

print("The last digit of 2 raised to the power of", power, "is:", last_digit)

# (b) One way to find out the last two digits of a number is to mod the number by 100. Write
# a program that asks the user to enter a power. Then find the last two digits of 2 raised to
# that power.
power = int(input("Enter a power: "))

last_two_digits = 2**power % 100

print("The last two digits of 2 raised to the power of", power, "is:", last_two_digits)

# (c) Write a program that asks the user to enter a power and how many digits they want.
# Find the last that many digits of 2 raised to the power the user entered.
import math

power = int(input("Enter a power: "))
num_digits = int(input("Enter the number of digits: "))

# Calculate the divisor based on the number of digits
divisor = 10**num_digits

last_digits = 2**power % divisor

print("The last", num_digits, "digits of 2 raised to the power of", power, "is:", last_digits)

# 11. Write a program that asks the user to enter a weight in kilograms. The program should
# convert it to pounds, printing the answer rounded to the nearest tenth of a pound
kilograms = float(input("Enter weight in kilograms: "))

pounds = kilograms * 2.20462

# Round the pounds to the nearest tenth
pounds_rounded = round(pounds, 1)

print(f"{kilograms} kilograms is approximately {pounds_rounded} pounds.")

# 12. Write a program that asks the user for a number and prints out the factorial of that number.
number = int(input("Enter a number: "))
factorial = 1

if number < 0:
  print("Factorial is not defined for negative numbers.")
elif number == 0:
  print("The factorial of 0 is 1")
else:
  for i in range(1, number + 1):
    factorial *= i

  print(f"The factorial of {number} is {factorial}")

#   13. Write a program that asks the user for a number and then prints out the sine, cosine, and
# tangent of that number.

number = float(input("Enter a number: "))

sine = math.sin(number)
cosine = math.cos(number)
tangent = math.tan(number)

print(f"The sine of {number} is {sine:.4f}")
print(f"The cosine of {number} is {cosine:.4f}")
print(f"The tangent of {number} is {tangent:.4f}")

# 14. Write a program that asks the user to enter an angle in degrees and prints out the sine of that
# angle
degrees = float(input("Enter an angle in degrees: "))

# Convert degrees to radians
radians = math.radians(degrees)

sine = math.sin(radians)

print(f"The sine of {degrees} degrees is {sine:.4f}")

# 15. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345◦
# in 15◦ increments. Each result should be rounded to 4 decimal places. Sample output is shown
# below:
# 0 --- 0.0 1.0
# 15 --- 0.2588 0.9659
# 30 --- 0.5 0.866
# ...
# 345 --- -0.2588 0.9659

for angle in range(0, 360, 15):
  radians = math.radians(angle)
  sine = round(math.sin(radians), 4)
  cosine = round(math.cos(radians), 4)
  print(f"{angle} --- {sine} {cosine}")

# 16. Below is described how to find the date of Easter in any year. Despite its intimidating appearance, this is not a hard problem. Note that bxc is the floor function, which for positive numbers
# just drops the decimal part of the number. For instance b3.14c = 3. The floor function is part
# of the math module.
# C = century (1900’s → C = 19)
# Y = year (all four digits)
# m = (15 + C − b C
# 4
# c − b 8C+13
# 25 c) mod 30
# n = (4 + C − b C
# 4
# c) mod 7
# a = Y mod 4
# b = Y mod 7
# c = Y mod 19
# d = (19c + m) mod 30
# e = (2a + 4b + 6d + n) mod 7
# Easter is either March (22+d +e) or April (d +e−9). There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year. 
import math

def easter_date(year):
  c = year // 100
  y = year % 100

  m = (15 + c - math.floor(c / 4) - math.floor((8 * c + 13) / 25)) % 30
  n = (4 + c - math.floor(c / 4)) % 7
  a = y % 4
  b = y % 7
  d = (19 * c + m) % 30
  e = (2 * a + 4 * b + 6 * d + n) % 7

  day = 22 + d + e

  if d == 29 and e == 6:
    month = 4
    day = 19
  elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 39]:
    month = 4
    day = 18
  elif day > 31:
    month = 4
    day -= 31
  else:
    month = 3

  return month, day

year = int(input("Enter a year: "))
month, day = easter_date(year)

print(f"Easter in {year} is on {month}/{day}")

# 17. A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.
year = int(input("Enter a year: "))
leap_years = 0

for year in range(1600, year + 1):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_years += 1

print(f"There have been {leap_years} leap years between 1600 and {year}")

# 18. Write a program that given an amount of change less than $1.00 will print out exactly how
# many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
# [Hint: the // operator may be useful.]
amount = float(input("Enter the amount of change (less than $1.00): "))

quarters = amount // 0.25
amount %= 0.25
dimes = amount // 0.10
amount %= 0.10
nickels = amount // 0.05
pennies = round(amount * 100)

print(f"Quarters: {int(quarters)}")
print(f"Dimes: {int(dimes)}")
print(f"Nickels: {int(nickels)}")
print(f"Pennies: {int(pennies)}")

# 19. Write a program that draws “modular rectangles” like the ones below. The user specifies the
# width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
# from left to right and top to bottom, but are all done mod 10. Below are examples of a 3 × 5
# rectangle and a 4 × 8.
# 0 1 2 3 4
# 5 6 7 8 9
# 0 1 2 3 4
# 0 1 2 3 4 5 6 7
# 8 9 0 1 2 3 4 5
# 6 7 8 9 0 1 2 3
# 4 5 6 7 8 9 0 1
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

for row in range(height):
  for col in range(width):
    print(f"{row * width + col:2d}", end=" ")
  print()

