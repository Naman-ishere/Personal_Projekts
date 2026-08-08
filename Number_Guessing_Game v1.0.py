import random 

while True:
    print("Welcome to the Number Guessing Game!")
    confirmation = input("Would you like to play? (y/n): ")
    good_confirmation = confirmation.lower().strip()
    
    if good_confirmation =="y":
        print("Great! Let's start the game.")
        