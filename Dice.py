import random

def dice():
    print("Welcome to the dice programme")
    print("To roll the dice, type 'roll'")
    print("To exit the programme, type 'exit'")
    action = input("What would you like to do?")
    while action != "exit":
        if action != "roll":
            print("Please enter a valid command")
            action = input("What would you like to do?")
        else:
            dice_roll = random.randint(1,6)
            print(f"You have rolled the number {dice_roll}")
            action = input("What would you like to do next?")

    print("Thank you for using the programme, have a nice day")

dice()