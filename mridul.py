# Rock/paper/scissors game!
import random

input("Welcome to the rock, paper, scissors game! Press enter to start.")
print()

user_score = 0
comp_score = 0
num_ties = 0


def question():
    # If user has played the game...
    played_before = input("Have you played rock,paper,scissors before? ").lower()
    # If user input is yes, then the output will be that program will continue...
    if played_before == "yes" or played_before == "y":
        played_before = "yes"
        print("-------------------")
        print("THE GAME BEGINS")
        print("-------------------")
    # If user input is no, then instructions will be shown...
    elif played_before == "no" or played_before == "n":
        print("-------------------")
        print("***HOW TO PLAY***")
        print("-------------------")
        print()
        print("1. Choose rock, paper or scissors")
        print("2. You will be against the computer")
        print("3. Rock beats scissors, scissors beats paper and paper beats rock")
        print(
            "4. If you win you get a point and vice versa, but if you and the computer choose the same option, it's a tie!")
        print("5. Whoever has the most wins at the end, wins!")
        print("GOOD LUCK")
        print()
        return


def selectcompchoice():
    comp_choice = random.choice(options)
    comp_choice.lower()
    return comp_choice


def selectuserchoice():
    user_choice = input("Please enter your choice - Rock, Paper or Scissors ")
    user_choice.lower()
    return user_choice


def compare(compchoice, userchoice):
    print("In comparison")
    if compchoice == "rock" and userchoice == "paper":
        winner = userchoice
        flag += 1

    elif userchoice == "rock" and compchoice == "paper":
        winner = compchoice
        flag += 0

    elif compchoice == "scissors" and userchoice == "paper":
        winner = compchoice
        flag += 0

    elif userchoice == "scissors" and compchoice == "paper":
        winner = userchoice
        flag += 1

    elif compchoice == "rock" and userchoice == "scissors":
        winner = compchoice
        flag += 0

    elif userchoice == "rock" and compchoice == "scissors":
        winner = userchoice
        flag += 1

    else:
        winner = "It's a tie!"
        flag = 2

    return flag


def history(user_choice_list, comp_choice_list, user_score, comp_score):
    print("COMPUTER'S LIST = ", comp_choices_list)
    print("USER'S LIST=", user_choices_list)
    return


ctr = 1
user_choices_list = []
comp_choices_list = []
rounds = 0
options = ['Rock', 'Paper', 'Scissors']

num_rounds=int(input("How many rounds do you wish to play? 0 for infinite play "))
if num_rounds == 0:
    print("You are in infinte mode - press xxx to exit")
yes_no = input("Press <ENTER> to continue - press xxx to exit")
while (yes_no != 'xxx'):
    comp_choice = selectcompchoice()
    user_choice = selectuserchoice()
    user_choices_list.append(user_choice)
    comp_choices_list.append(comp_choice)
    print(wins_user, wins_comp)

winner = compare(comp_choice, user_choice)
print(winner)
if winner == 1:
    user_score += 1
elif winner == 0:
    comp_score += 1

if user_score > comp_score:
    print("You win!")
elif user_score == comp_score:
    print("Tie")
else:
    print("Comp wins!")

print()
print("------STATS------")
print("Your number of wins are", user_score)
print("Number of computer wins are", comp_score)
print("You and the computer have:", num_ties, "games tied")
print()

print("------STAT HISTORY------")
history(user_choices_list, comp_choices_list)

print("You are in infinite mode")
yes_no = input("Press ENTER> to continue - press xxx to exit")

if yes_no == 'xxx':
    print("Thank you for playing!")
    exit(0)