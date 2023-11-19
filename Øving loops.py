import os

target_number = int(input("Target number: "))

mistakes_allowed = int(input("How many mistakes allowed: "))

os.system('cls' if os.name == 'nt' else 'clear')
x=0
while True:

    guess = int(input("Guess a number: "))

    if mistakes_allowed == x:
        print("Too many guesses, you lose!")
        break

    if guess == target_number:
        print("Correct")
        break
    elif guess > target_number:
        x += 1
        print("lower")
        print(f"You have {mistakes_allowed - x} tries left")
        
    else:
        print("higher")
        x += 1
        print(f"You have {mistakes_allowed - x} tries left")
        