import random

def lottery_game():
    lottery = random.randint(10, 99)
    user_input = int(input("Enter a two-digit number: "))
    
    lottery_digit1, lottery_digit2 = divmod(lottery, 10)
    user_digit1, user_digit2 = divmod(user_input, 10)
    
    print(f"Lottery number: {lottery}")
    
    if user_input == lottery:
        print("Congratulations! You won $10,000!")
    elif sorted([lottery_digit1, lottery_digit2]) == sorted([user_digit1, user_digit2]):
        print("Great! You won $5,000!")
    elif user_digit1 in [lottery_digit1, lottery_digit2] or user_digit2 in [lottery_digit1, lottery_digit2]:
        print("Good! You won $2,000!")
    else:
        print("Sorry, better luck next time!")

lottery_game()