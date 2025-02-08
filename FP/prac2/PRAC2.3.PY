import random

def guess_number():
    magic_number = random.randint(0, 100)
    print("Guess a magic number between 0 and 100")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 0 or guess > 100:
                print("Please enter a number between 0 and 100.")
                continue
            if guess < magic_number:
                print("Your guess is too low")
            elif guess > magic_number:
                print("Your guess is too high")
            else:
                print(f"Yes, the number is {guess}")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guess_number()