import random 

options = ["rock", "paper", "scissors"]
player_choice = input("enter your choice (rock,paper ,scissors): ").lower()
computer_choice = random.choice(options)
print(f"Computer chose: {computer_choice}")

if player_choice == computer_choice:
    print("its a tie")
elif (player_choice == "rock" and computer_choice == "scissors"):
    print("you win")
elif (player_choice == "paper" and computer_choice == "rock"):
    print("you win")
elif (player_choice == "scissors" and computer_choice == "paper"):
    print("you win")
else:
    print("you lose")