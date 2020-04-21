#Modified Number Guessing Game

#User select the level of game

import random
play = True
while play:
    try:
        level = int(input("Choose Game Level: 1 = Easy, 2 = Medium, 3 = Hard): "))
        if level == 1:
            top = 10
            tries = 6
        elif level == 2:
            top = 20
            tries = 4
        elif level == 3:
            top = 50
            tries = 3
        else:
            print("Choose between 1 and 3")
#Print statements for chosen level to tell how many guesses user gets
        if level == 1:
            print("You have chosen 'Easy' and you have 6 guesses")
        if level == 2:
            print("You have chosen 'Medium' and you have 4 guesses")
        if level == 3:
            print("You have chosen 'Hard' and you have 3 guesses")
        elif level != 1 and level != 2 and level != 3:
            print("Invalid input!")
    except (NameError, ValueError):
        print("Enter number between 1 and 3")
#select number of guesses depending on difficulty selected
#Level for 1 for Easy
    while level ==1:
        number = random.randint(1, 10)
        print("Try to guess the number between 1 and 10!")
        try:
            guessesTaken = 0
            tries = 10
            while guessesTaken <= tries:
                guess = int(input("Take a guess: "))
                if guess > 10:
                    print("Choose a number between 1 and 10")
                if guess != number:
                    print("Try Again.")
                    print(f" Your chance remain {tries - 5}")
                    guessesTaken += 1
                    tries -= 1
                if guess == number:
                    print("You got it right! Good Job!")
                    break
        except ValueError:
            print("Number between 1 and 10 only")
        break

#Level for 2 for Medium
    while level ==2:
        number = random.randint(1, 20)
        print("Try to guess the number between 1 and 20!")
        try:
            guessesTaken = 0
            tries = 6
            while guessesTaken <= tries:
                guess = int(input("Take a guess: "))
                if guess > 20:
                    print("Choose a number between 1 and 20")
                if guess != number:
                    print("Try Again.")
                    print(f" Your chance remain {tries - 3}")
                    guessesTaken += 1
                    tries -= 1
                if guess == number:
                    print("You got it right! Good Job!")
                    break
        except ValueError:
            print("Number between 1 and 10 only")
        break

#Level for 3 for Hard
    while level == 3:
        number = random.randint(1, 50)
        print("Try to guess the number between 1 and 50!")
        try:
            guessesTaken = 0
            tries = 4
            while guessesTaken <= tries:
                guess = int(input("Take a guess: "))
                if guess > 50:
                    print("Choose a number between 1 and 50")
                if guess != number:
                    print("Try Again.")
                    print(f" Your chance remain {tries - 2}")
                    guessesTaken += 1
                    tries -= 1
                if guess == number:
                    print("You got it right! Good Job!")
                    break
        except ValueError:
            print("Number between 1 and 10 only")
        break

#Play again loop that attaches to original statement that allows you to quit or play again.
    count = 1
    number = str(number)
    print("Nope. The number was: " + number)
    again = str(input("Game Over! \n Do you want to play again? \n Type yes or no: "))
    if again == "no":
        play = False
    else:
        print("Start all over!")