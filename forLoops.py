# 1. Write a program that prints your name 100 times.
for name in range(100):
    print(name+1, "- Kennedy") 

#  2. Write a program to fill the screen horizontally and vertically with your name. [Hint: add the
#  option end='' into the print function to fill the screen horizontally.]
# Fill the screen horizontally
for i in range(50):
    print("Kennedy", end="")

print()  # Move to the next line

# Fill the screen vertically
for i in range(20):
    print("Kennedy")

#  3. Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The
#  output should look like the output below.
#  1 Your name
#  2 Your name
#  3 Your name
#  4 Your name
#  ...
#  100 Your name
for name in range(100):
    print(name+1, "Kennedy")

# 4. Write a program that prints out a list of the integers from 1 to 20 and their squares. The output
#  should look like this:
#  1--- 1
#  2--- 4
#  3--- 9
#  ...
#  20--- 400
for intengers in range(1, 21):
    print(intengers,"---",intengers*intengers)

#  5. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, ..., 83, 86, 89.
for num in range(8, 90, 3):
    print(num, end=", ")
print('\n')

# 6. Write a program that uses a for loop to print the numbers 100, 98, 96, ..., 4, 2.
for reverse in range(100, 0, -2):
    print(reverse, end=" ")
print('\n')

# 7. Write a program that uses exactly four for loops to print the sequence of letters below.
#  AAAAAAAAAABBBBBBBCDCDCDCDEFFFFFFG
for A in range(10):
    print("A")
for B in range(7):
    print("B")
for CD in range(4):
    print("CD")
print("E")
for F in range(6):
    print('F')
print('G')
print('\n')

# 8. Write a program that asks the user for their name and how many times to print it. The pro
# gram should print out the user’s name the specified number of times.
name = input('Enter Your Name: ')
loop = int(input("Number of times to loop: "))
for l in range(loop):
    print(l+1, name)

# 9. The Fibonacci numbers are the sequence below, where the first two numbers are 1, and each
#  number thereafter is the sum of the two preceding numbers. Write a program that asks the
#  user how manyFibonacci numbers to print and then prints that many.
#  1,1,2,3,5,8,13,21,34,55,89...
n = int(input("Enter the number of Fibonacci numbers to print: "))

# Initialize the first two Fibonacci numbers
fib1, fib2 = 1, 1

print(fib1, fib2, end=" ")

# Generate and print the remaining Fibonacci numbers
for i in range(2, n):
    fib3 = fib1 + fib2
    print(fib3, end=" ")
    fib1, fib2 = fib2, fib3
print('\n')

# 10. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
#  high the box should be. [Hint: print('*'*10) prints ten asterisks.]
#  *******************
#  *******************
#  *******************
#  *******************
for box in range(4):
    print('*'*25)

# 11. Use a for loop to print a box like the one below. Allow the user to specify how wide and how
#  high the box should be.
#  *******************
#  *                 *
#  *                 *
#  *******************
width = int(input("Enter the width of the box: "))
height = int(input("Enter the height of the box: "))

# Print the top row
print('*' * width)

# Print the middle rows
for i in range(height - 2):
    print('*' + ' ' * (width - 2) + '*')

# Print the bottom row
print('*' * width)

#  12. Use a for loop to print a triangle like the one below. Allow the user to specify how high the
#  triangle should be.
#  *
#  **
#  ***
#  ****
height = int(input("Enter the height of the triangle: "))

for i in range(1, height + 1):
    print('*' * i)

# 13. Use a for loop to print an upside down triangle like the one below. Allow the user to specify
#  how high the triangle should be.
#  ****
#  ***
#  **
#  *
height = int(input("Enter the height of the triangle: "))

for i in range(height, 0, -1):
    print('*' * i)

# 14. Use for loops to print a diamond like the one below. Allow the user to specify how high the
#  diamond should be.
#  *
#  ***
#  *****
#  *******
#  *****
#  ***
#  *
height = int(input("Enter the height of the diamond: "))

# Print the top half of the diamond
for i in range(1, height + 1, 2):
    print(' ' * ((height - i) // 2) + '*' * i)

# Print the bottom half of the diamond
for i in range(height - 2, 0, -2):
    print(' ' * ((height - i) // 2) + '*' * i)

#15. Write a program that prints a giant letter A like the one below. Allow the user to specify how
#  large the letter should be.
#      *
#    *   *
#    *****
#  *       *
# *         *
height = int(input("Enter the height of the letter A: "))

# Print the top half of the A
for i in range(1, height // 2 + 1):
    print(' ' * (height - i) + '*' * (2 * i - 1))

# Print the middle row of the A
print(' ' * (height // 2) + '*')

# Print the bottom half of the A
for i in range(height // 2 - 1, 0, -1):
    print(' ' * (height - i) + '*' * (2 * i - 1))