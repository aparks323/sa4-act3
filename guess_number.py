number = 10
print("I'm thinking of a number...")
guess = (input("What number am I thinking of? (Press q to quit.) "))
numguess = 1
if guess == number:
    print("Congratulations! You guessed the right number.")
elif guess != number:
        print(f"Sorry! The number was {number}.")
        guess = (input("What number am I thinking of? (Press q to quit.) "))
        numguess += 1
        print(f'You have guessed {numguess} times.')
elif guess == 'q':
    print("Goodbye!")


