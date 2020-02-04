import random

#-------------------
#Welcome to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!



#striving for above output



print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

options = ["rock", "paper", "scissors"]
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

if user_choice not in options:
    print("OOPS! Invalid selection!")
    exit()

print(f"You chose: '{user_choice}'")

computer_choice = random.choice(options)

print(f"The computer chose: '{computer_choice}'")


###### Determining winner ######

winner = ""

if user_choice == "rock" and computer_choice == "scissors":
    winner = "user"
elif user_choice == "paper" and computer_choice == "rock":
    winner = "user"
elif user_choice == "scissors" and computer_choice == "paper":
    winner = "user"
elif user_choice == computer_choice:
    winner = "both"
else:
    winner = "computer"


###### Printing results ######


print("-------------------")

if winner == "user":
    print("You won! Yay!")
elif winner == "computer":
    print("Oh, the computer won. It's ok.")
else:
    print("Wow, you tied!")


print("-------------------")
print("Thanks for playing. Please play again!")