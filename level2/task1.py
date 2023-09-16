import random
n = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100 ="))
while guess != n:
    if guess > n:
        print("you have guessed a high number ")
    else:
        print("Your guess is too low.")
    guess = int(input("Guess again:"))
if guess == n:
    print("Congratulations! You guessed the number correctly.")