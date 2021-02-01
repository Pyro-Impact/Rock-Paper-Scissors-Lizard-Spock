import random

print("Welcome to the Rock Paper Scissors Lizard Spock game!")

while True:
    while True:
        players_choice = input("Choose Rock, Paper, Scissors, Lizard, or Spock:")
        if players_choice.title() in ["Rock", "Paper", "Scissors", "Lizard", "Spock"]:
            break
        print("Please enter a valid input.")

    computer_actions = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    computer_choice = random.choice(computer_actions)

    key = {"Scissors": ["Paper", "Lizard"],
           "Paper": ["Rock", "Spock"],
           "Rock": ["Scissors", "Lizard"],
           "Lizard": ["Paper", "Spock"],
           "Spock": ["Scissors", "Rock"]}

    verb_details = {"Rock": "crushes",
                    "Paper": "covers",
                    "Scissors": "cuts",
                    "Lizard": "poisons",
                    "Spock": "shoots"}

    draw = {"Rock": "bash",
            "Paper": "slap",
            "Scissors": "scratch",
            "Spock": "shoot",
            "Lizard": "ignore"}

    def final_result():
        player_choice_t = players_choice.title()

        print(f"You chose {player_choice_t}, The computer chose {computer_choice}")

        if computer_choice in key[player_choice_t]:
            win = f"{player_choice_t} {verb_details[players_choice.title()]} {computer_choice}. You win."
            return win
        elif player_choice_t in key[computer_choice]:
            lose = f"{computer_choice} {verb_details[computer_choice]} {player_choice_t}. You lose."
            return lose
        else:
            tie = f"The {player_choice_t}(s) {draw[player_choice_t]} each other, and it's a draw."
            return tie

    print(final_result())

    while True:
        cont_choice = input("Would you like to play again? Type (yes/no): ")
        if cont_choice.lower() in ("yes", "no"):
            break
        print("Invalid input.")

    if cont_choice.lower() == "yes":
        continue
    else:
        print("Thanks for playing!")
        break
