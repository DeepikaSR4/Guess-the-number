from random import randint
x = randint(1,100)
guess = 0
print("Guess a number between 1 and and 100")
while True:
    num = int(input("\nGuess the number\n"))
    guess = guess+1
    if(num>x):
        print("Uh! Your guess is higher\n")
    elif(num<x):
        print("Oh! Your guess is lower\n")
    else:
        print("Wohooo!! You guessed it right\n")
        g = str(guess)
        print("You did it in\t"+g+"\tguesses")
        break


