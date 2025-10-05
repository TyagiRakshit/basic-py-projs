import random
list1 = ["r","p","s"]
choice = input("do u want to play:(y/n)")
while choice.lower() == "y":
 try :
    print("let play !!!")
    comp_choice = random.choice(list1)
    user_choice = input("choose -> rock(r),paper(p),scissor(s)")
    if user_choice == comp_choice:
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("OHH we got same ")
    elif user_choice == "r" and comp_choice == "p":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! i won")
    elif user_choice == "r" and comp_choice == "s":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! u won")
    elif user_choice == "p" and comp_choice == "r":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! u won")
    elif user_choice == "p" and comp_choice == "s":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! i won")
    elif user_choice == "s" and comp_choice == "p":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! u won")
    elif user_choice == "s" and comp_choice == "r":
        print(f"i choose {comp_choice} and u choose {user_choice}")
        print("hey! i won")
    else:
        print("INVALID CHOICE!!!!")
        break
    choice = input("do u want to cont...>>>y/n:")

 except ValueError:
       print("INVALID  CHOICE!!!")
       break
