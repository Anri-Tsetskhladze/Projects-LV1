import random

def generate_code(length=4):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

def get_feedback(secret, guess):
    if len(secret) != len(guess):
        return "Invalid input. Make sure your guess has the same length as the secret code."
    
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    
    return bulls, cows

def play_mastermind():
    print("Welcome to Mastermind!")
    print("Player 1, please set a multi-digit number (digits only, no spaces):")
    
    secret_code = input("Secret Code: ")
    while not secret_code.isdigit():
        print("Invalid input. Please enter digits only.")
        secret_code = input("Secret Code: ")

    attempts = 0
    while True:
        print("Player 2, please guess the multi-digit number:")
        guess = input("Your Guess: ")
        
        while not guess.isdigit() or len(guess) != len(secret_code):
            print(f"Invalid input. Make sure your guess has {len(secret_code)} digits.")
            guess = input("Your Guess: ")
        
        attempts += 1
        bulls, cows = get_feedback(secret_code, guess)
        
        if bulls == len(secret_code):
            print(f"Congratulations! You've guessed the correct code in {attempts} attempts.")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")
            print("Try again!")
    
    print("\nNow, Player 2 sets the code and Player 1 guesses.")
    
    secret_code = generate_code(len(secret_code))
    attempts = 0
    while True:
        print("Player 1, please guess the multi-digit number:")
        guess = input("Your Guess: ")
        
        while not guess.isdigit() or len(guess) != len(secret_code):
            print(f"Invalid input. Make sure your guess has {len(secret_code)} digits.")
            guess = input("Your Guess: ")
        
        attempts += 1
        bulls, cows = get_feedback(secret_code, guess)
        
        if bulls == len(secret_code):
            print(f"Congratulations! You've guessed the correct code in {attempts} attempts.")
            break
        else:
            print(f"Bulls: {bulls}, Cows: {cows}")
            print("Try again!")

if __name__ == "__main__":
    play_mastermind()