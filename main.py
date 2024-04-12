import random
rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
    '''

paper = '''
    _______
---'   ____)____
            ______)
            _______)
            _______)
---.__________)
    '''

scissors = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
    '''


game_images = [rock, paper, scissors]

def get_player_choice():
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
    while player_choice < 0 or player_choice > 3:
        print("Invalid response. Please type 0 for Rock, 1 for Paper, and 2 for Scissors.")
        player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))
    return player_choice

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        print("It's a draw.")
    elif (player_choice == 0 and cpu_choice == 2) or \
         (player_choice == 1 and cpu_choice == 0) or \
         (player_choice == 2 and cpu_choice == 1):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    continue_game = 'y'
    while continue_game == 'Y' or 'y':
        user_choice = get_player_choice()
        cpu_choice = random.randint(0,2)
        print(game_images[user_choice])
        print("Computer chose:", cpu_choice)
        print(game_images[cpu_choice])
        print(determine_winner(user_choice, cpu_choice))
        continue_game = input("Do you want to play again? (y/n): ")
        if continue_game == 'N' or 'n':
            return
if __name__ == "__main__":
    main()