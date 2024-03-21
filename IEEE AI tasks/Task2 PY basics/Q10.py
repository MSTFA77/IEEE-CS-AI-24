import random
def guessing_game():
    secret_number = random.randint(1, 100)
    num_guesses = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        num_guesses += 1
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} correctly in {num_guesses} guesses.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
guessing_game()
