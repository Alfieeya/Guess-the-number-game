import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        try:
            guess = int(input("Guess the lucky number between 1 and 50: "))
            if guess < 1 or guess > 50:
                print("Please enter a number within the range of 1 to 50.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if guess < lucky_num:
            print("Too low! Try again.")
        elif guess > lucky_num:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the lucky number {lucky_num}!")
            break

    print("Thank you for playing!")

play_game()