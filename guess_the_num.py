import random
print("Welcome to the game of GUESS THE NUMBER!")
print("--ALL THE BEST--")

num = random.randint(0,100)

while True:
        choice = int(input("Guess any number between 0-100: "))
        if(choice==num):
            print("Congratulations!")
            print("You guessed it right")
            break
        elif(choice>num):
            print(f"LESSER than {choice}")
        elif(choice<num):
            print(f"GREATER than  {choice}")
