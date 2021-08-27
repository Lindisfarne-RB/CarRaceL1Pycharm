# functions go here
import random


def welcome(name):
    print("Welcome", name)


def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # if they say yes, output 'program continues'
        if response == "yes" or response == "y":
            response = "yes"
            return response
            print("program continues")
        # if they say no, output 'display instructions'
        elif response == "no" or response == "n":
            response = "no"
            return response
            print("display instructions")
        else:
            print("please answer yes / no")


def instructions():
    print("*****How to Play*****")
    print("*Select rock(r), paper(p) or sissors(s)")
    print("*The computer will also randomly select one of the three options")
    print("*Rock beats scissors")
    print("*Scissors beats paper")
    print("*Paper beats rock")
    return ""


def pickcompchoice():
    comp_choice = random.choice(options)
    comp_choice.lower()
    return comp_choice


def choice_checker(question):
    valid = False
    while not valid:
        response = input(question).lower()

        # ask user for choice
        if response == "rock" or response == "r":
            response = "rock"
            return response
        elif response == "paper" or response == "p":
            response = "paper"
            return response
        elif response == "scissors" or response == "s":
            response = "scissors"
            return response
        else:
            print("please choose rock / paper / scissors (r / p / s)")


def compare(user_choice, comp_choice):
    # possible outcomes of rock, paper and scissor

    if comp_choice == "rock" and user_choice == "paper":
        winner = user_choice

    elif user_choice == "rock" and comp_choice == "paper":
        winner = comp_choice

    elif comp_choice == "scissors" and user_choice == "paper":
        winner = comp_choice

    elif user_choice == "scissors" and comp_choice == "paper":
        winner = user_choice

    elif comp_choice == "scissors" and user_choice == "rock":
        winner = user_choice

    elif user_choice == "scissors" and comp_choice == "rock":
        winner = comp_choice

    elif comp_choice == "rock" and user_choice == "paper":
        winner = user_choice

    elif user_choice == "rock" and comp_choice == "paper":
        winner = user_choice

    else:
        pass
    return winner


# main routine goes here
name = input("What is your name?")
welcome(name)

played_before = yes_no("Have you played before?")

if played_before == "no":
    instructions()
print("You chose {}".format(played_before))
print("program continues")
print()

# ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper / scissors (r / p / s)")

print(name, ": {}".format(user_choice))
# rounds = int(input("how many rounds would you like to play?, enter 0 for infinite play"))

# computer randomly choses rock, paper, scissors
options = ['rock', 'paper', 'scissors']
comp_choice = pickcompchoice()
print("computer : {}".format(comp_choice))

winner = compare(user_choice, comp_choice)
print("{} won".format(winner))