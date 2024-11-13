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

