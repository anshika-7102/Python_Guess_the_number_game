import random
num = random.randint(1,50)

print("Welcome to the number guessing game. We have a number that needs to be guessed. you have 5 chances.")
print("The secret number is between 1 and 50")

for i in range(5,0,-1):
    print(f"You have {i} attempts left")
    choice = int(input("Enter your guess: "))
    if(choice == num):
        print("Congratulations, your guess is right!")
    elif(choice<num):
        print("Your guess is wrong!, Try higher")
    elif(choice>num):
        print("Your guess is wrong!, Try lower")
    else:
        print("Invalid input.")
print(f"The number was {num}")
print("GAME OVER!")
print("Thank you for playing!")