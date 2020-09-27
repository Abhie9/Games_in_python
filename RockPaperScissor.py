import random

Choice=["rock","paper","scissor"]
while True:
    Computer= random.choice(Choice)
    userIn=input("Please choose any from 'R' for Rock, 'P' for Paper, 'S' for Scissor and to exit the game Choose 'E': ")[0].lower()
    if "s" in userIn or "r" in userIn or "p" in userIn or "e" in userIn:
        if Computer == "rock" and userIn == "p":
            print("Well Played Computer's Choice was",Computer)
        elif Computer == "rock" and userIn == "s":
            print("Oops! I win my Choice was",Computer)
        elif Computer == "rock" and userIn == "r":
            print("tough one! my choice was same as yours")
        if Computer == "scissor" and userIn == "r":
            print("Well Played Computer's Choice was",Computer)
        elif Computer == "scissor" and userIn == "p":
            print("Oops! I win my Choice was",Computer)
        elif Computer == "scissor" and userIn == "s":
            print("tough one! my choice was same as yours")
        if Computer == "paper" and userIn == "r":
            print("Well Played Computer's Choice was",Computer)
        elif Computer == "paper" and userIn == "s":
            print("Oops! I win my Choice was",Computer)
        elif Computer == "paper" and userIn == "p":
            print("tough one! my choice was same as yours")
        if userIn == "e":
            print("thanks for playing!! :)")
            break
    else:
        print("please enter valid option")