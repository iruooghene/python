digit = int(input("Enter a five digit number eg 12543: "))
first_number = digit // 10000

second_number = (digit % 10000) // 1000

third_number = (digit % 1000) // 100

fourth_number = (digit % 100) // 10

fifth_number = digit % 10 

print("Seperation is: ", first_number ,second_number,third_number,fourth_number,fifth_number)