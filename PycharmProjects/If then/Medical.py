import random

number = random.randint(1,10)
tries = 1

uname = input("Hello, Username Please")

print("Hello", uname + ".")

question = input("Would you like to play a game? [y/n]")
if question == "n":
    print("goodbye")

elif question == "y":
    print("I'm thinking of  a number between 1 & 10")
    guess = int(input("have a guess"))
    while guess != number:
        if guess > number:
            print("Lower")
        elif guess < number:
            print("Higher")
        tries += 1
        guess = int(input("Try Again"))
    print("Correct! It was", number, "you tried", tries, "times")