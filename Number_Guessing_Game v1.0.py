import random 

print("Welcome to the Number Guessing Game!")
confirmation = input("Would you like to play? (y/n): ")
good_confirmation = confirmation.lower().strip()
guesses = []

if good_confirmation =="y":
    while True:
        print("Great! Let's start the game.")
        luckyNumber = random.randint(1,100)
        print(luckyNumber)

        guess = int(input("Enter your number: "))
        if type(guess) == int:
            if guess < luckyNumber: 
                print("Think higher!! Be ambitious.......")
                guesses.append(guess)
            elif guess > luckyNumber: 
                print("Think lower!! Dont be greedy.......")
                guesses.append(guess)
            else:
                guesses.append(guess)
                print("Congratulationssss!!! You have won the game.")
                print("You took total of", len(guesses), "number of attempts to guess the number.")
                playAgain = input("Do you want to play again? (y/n): ")
                good_playAgain = playAgain.lower().strip()
                if good_playAgain == "y":
                    guesses.clear()
                    print("Great! Let's start the game.")
                    continue
                elif good_playAgain == "n":
                    print("Thanks for playing!")
                    break
        else:
            print("Please enter a valid number as an output.")
else:
    print("Bye Bye :(")           
        