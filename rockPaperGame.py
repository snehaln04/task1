import random

user_score = 0
comp_score = 0
ties = 0

print("Rules for the game: ")
print("""
    1. Paper VS Rock ---> Paper
    2. Rock VS Scissors ---> Rock
    3. Scissosrs VS Paper ---> Scissors """)

while True:
    print(""" Choices are -
          1. ROCK
          2. PAPER
          3. SCISSORS""")
    choice = int(input("Enter your choice from 1-3 : "))
    print()

    while choice > 3 or choice < 1:
        choice = int(input("Please enter a valid input: "))

    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print("User's choice is ", user_choice)
    print("Now it's computer's turn.....")
    print()

    computer = random.randint(1, 3)
    if computer == 1:
        comp_choice = "Rock"
    elif computer == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print("Computer's choice is ", comp_choice)
    print()

    if user_choice == comp_choice:
        print("It's a tie")
        ties += 1
    elif (user_choice == "Rock" and comp_choice == "Scissors") or (user_choice == "Scissors" and comp_choice == "Paper") or (user_choice == "Paper" and comp_choice == "Rock"):
        print("You win")
        user_score += 1
    else:
        print("You lose")
        comp_score += 1

    print("Scores are:")
    print("Your score is: ", user_score)
    print("Computer's score is: ", comp_score)
    print("Ties: ", ties)

    play_again = input("Do you want to play again? (Yes/No): ")
    if play_again.lower() != "yes":
        print("GAME OVER......")
        print("Thanks for playing.....")
        break
