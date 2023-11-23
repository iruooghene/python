# 2.12 investment return

principal = int(input("Enter amount invested: "))
rate_of_return= int(input("Enter rate of return: "))
number_of_years = int(input("Enter number of years: "))
m = rate_of_return / 100
print(m)

amount_on_deposit =principal*(1 + m)**number_of_years
print("amount_on_deposit is", amount_on_deposit)