number1 = int(input("Enter an integer: "))
number2 = int(input("Enter an integer: "))
number3 = int(input("Enter an integer: "))

sum = number1 + number2 + number3
print(sum)

average = sum / 3
print(average)

product = number1 * number2 * number3
print(product)

if number1 > number2:
   if number1 > number3:
      print("highest is:", number1)
if number2 > number1:
   if number2 > number3:
      print("highest is:", number2)
if number3 > number1:
   if number3 > number2:
      print ("highest is:", number3)

if number1 < number2:
   if number1 < number3:
      print("Lowest is:", number1)
if number2 < number1:
   if number2 < number3:
      print("Lowest is:", number2)
if number3 < number1:
   if number3 < number2:
      print("Lowest is:", number3)