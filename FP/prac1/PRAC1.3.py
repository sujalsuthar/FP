import random

number = random.randint(0, 1000)
print(f"Generated number: {number}")

number_str = str(number)

sum_of_digits = 0


for digit in number_str:
    sum_of_digits += int(digit)

print(f"The sum of the digits is {sum_of_digits}")
