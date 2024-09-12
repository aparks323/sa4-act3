number = 10
print("I'm thinking of a number...")
guess = (input("What number am I thinking of? (Press q to quit.) "))

if guess == number:
    print("Congratulations! You guessed the right number.")
elif guess != number:
        print(f"Sorry! The number was {number}.")
        guess = (input("What number am I thinking of? (Press q to quit.) "))

elif guess > number:
     print("Guess too high.")
elif guess < number:
     print("Guess is too low.")
elif guess == 'q':
    print("Goodbye!")

