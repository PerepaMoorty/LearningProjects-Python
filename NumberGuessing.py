import random

print("WELCOME TO NUMBER GUESSER!")
print("The number will be chosen at random between 1 and 100")
print("And You have only 7 Tries to Guess the Random Number")

CHOSEN = random.randrange(1, 100)
trials = 7
won = False

while(trials > 0):
    trials -= 1
    guess = int(input("Enter your Guess: "))
    if(guess > CHOSEN): print("Try Lower")
    elif(guess < CHOSEN): print("Try Higher")
    else: 
        print("You Got it in: ", 7 - trials)
        print("The Random Number was indeed: ", guess)
        won = True
        break

if(not won): 
    print("Better Luck Next Time!\nThe Chosen Number was - ", CHOSEN)