amount = float(input("Enter an amount in double, for example 11.56: "))

cents = int(round(amount * 100))

dollars = cents // 100
cents %= 100

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print(f"Your amount {amount} consists of")
print(f"{dollars} dollars")
print(f"{quarters} quarters")
print(f"{dimes} dimes")
print(f"{nickels} nickels")
print(f"{pennies} pennies")