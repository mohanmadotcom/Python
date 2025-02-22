import random

game_images = ["0", "1", "2"]

user_choice = int(input("What do you choose? Type 0, 1, or 2:\n"))

if 0 <= user_choice <= 2:
    print(f"You chose: {game_images[user_choice]}")
    
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice. You lose!")
