# this is 1st basic project of python
import random
user = input("enter ur name:\n")
def play(a):
    print(f"HEY ! {a} , Welcome to the game ")
    choice = input("do u want to play the game? (y/n) ")
    if choice.lower() != "y" and choice.lower()!= "n":
        print("Invalid choice!")
    else :
     while choice.lower() == "y":
        print("let roll!!!")
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"{die1},{die2}")
        choice = input("do u want to  cont>>>(y/n)")



play(user)