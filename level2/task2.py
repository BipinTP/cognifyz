import random
lower_limit = 1
upper_limit = 50
random_number = random.randint(lower_limit, upper_limit)
num_guess = 0
max_guess = 3
while num_guess < max_guess:
    guess = int(input("Guess the number between {} and {}: ".format(lower_limit, upper_limit)))
    num_guess += 1
    if guess == random_number:
        print("Congratulations! You guessed the number in {} guesses.".format(num_guess))
        break
    elif guess > random_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

if num_guess == max_guess:
    print("Sorry, you ran out of guesses. The number was {}.".format(random_number))