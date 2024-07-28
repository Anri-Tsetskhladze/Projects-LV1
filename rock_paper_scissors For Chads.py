import random

user_wins = 0
computer_wins = 0

options = ["chico", "jordan", "nikita mogger", "bts"]

while True:
    user_input = input("Type Chico/Jordan/Nikita Mogger/BTS or E to quit: ").lower()
    if user_input == "e":
        break

    if user_input not in options:
        print("Invalid input. Please choose Chico, Jordan, Nikita Mogger, or BTS.")
        continue

    random_number = random.randint(0, 3)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "chico" and computer_pick == "jordan":
        print("You won!")
        user_wins += 1

    elif user_input == "jordan" and computer_pick == "bts":
        print("You won!")
        user_wins += 1

    elif user_input == "nikita mogger" and computer_pick == "bts":
        print("You won!")
        user_wins += 1

    elif user_input == "bts" and computer_pick == "chico":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
