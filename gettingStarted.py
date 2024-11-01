print('******************\n******************\n******************\n******************\n\n\n\n\n\n')
print('**********\n*        *\n*        *\n**********')
print('*\n**\n***\n****')
print((512-282)/(47*48+5))
print("Hi 😀! Please enter a number to calculate its square")
x = int(input('Enter a number: '))
print('The square of: ', x , ' is ', x*x)
print('Enter a number to generate a sequence: ')
y = int(input('Enter a number: '))
print(y, 2*y, 3*y, 4*y, 5*y, sep='---')
print('Enter your weight in kg to convert to pounds')
weight = int(input('Enter your weight in kg: '))
pound = weight * 2.2
print('Your weight in pounds is: ', pound)
print("Hello there 😀! Please enter three numbers so that we can calculate the average for you.")
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
num3 = int(input('Enter third number: '))
total = num1 + num2 + num3
average = total/3
print("Thank you 😀! The total sum is: ", total, " And the average is: ", average)
print('Hello dear customer 😀! Please enter your percentage tip and meal price to generate your bill.')
meal_price = int(input("Enter Meal Price: "))
percentage_tip = int(input("Enter percentage tip: "))
tip_amount = (percentage_tip/100) * meal_price
total_bill = meal_price + tip_amount
print("Thank you 😀! Your tip amount is: ", tip_amount, "\nAmount to pay: ", total_bill, "\nThank you😀 for eating with us! Welcome again!")