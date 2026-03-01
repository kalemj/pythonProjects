#prj 2
import random

def guess():
    print(f"I have guessed a random number!")
    guess = 0
    num = random.randint(1,100)
    attempts = 0
    while guess != num:
        guess = int(input(f"Guess here: "))
        if guess < num:
            print(f"{guess} is below random number. Attempts: {attempts+1}")
            attempts += 1
        elif guess > num:
            print(f"{guess} is above random number. Attempts: {attempts+1}")
            attempts += 1
        else:
            print(f"It was {num}. Well done!")
            break

def computerGuess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f'Is {guess} too high? (y)es / (n)o / (c)orrect')
        if feedback == 'y':
           high = guess -1 
        elif feedback == 'n':
            low = guess + 1
        else:
            print("I got it right!")
            break


choice = input("Do u want to play the computer or have the computer play you? \nPlay AI - Input AI \nAI Guess - Input Guess")
if choice.upper() == "GUESS":
    x = int(input("What is ur number?"))
    computerGuess(x)
elif choice.upper() == "AI":
    guess()
else:
    print("You didn't chose a right game")



