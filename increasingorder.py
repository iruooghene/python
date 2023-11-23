number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))

if number1 > number2 and number1 > number3:
   highest = number1
if number2 > number1 and number2 > number2:
   highest = number2
if number3 > number1 and number3 > number2:
   highest = number3
if number1 < number2 and number1 < number3:
   lowest = number1
if number2 < number1 and number2 < number3:
   lowest = number2
if number3 < number1 and number3 < number2:
   lowest = number3

if number1 != number2 and number1 != number3:
   middle = number1
if number2 != number1 and number2 != number3:
   middle = number2
if number3 != number1 and number3 != number2:
   middle = number3
print( lowest, middle, highest )