import random
print("LEt`s play tha Black JAck Game!\n")
def fisrt_oponent():
    result_1 = 0
    name_1 = input("The first player\nYour name?\n")
    print("Hello " + name_1)
    while True:
        x = input("Do you need card? \ny - yes\nn - no\nYour choise: ")
        if x == "n":
            print(name_1, "your result is:", result_1)
            return(result_1)
        elif x == "y": 
            koloda = random.randint(2, 11)
            result_1 += koloda
        else:
            exit()
        print(result_1)
        if result_1 > 21:
            print("You lose!\nGood Bye!")
            exit()
def second_oponent():
    result_2 = 0
    name_2 = input("The second player\nYour name?\n")
    print("Hello " + name_2)
    while True:
        x = input("Do you need card? \ny - yes\nn - no\nYour choise: ")
        if x == "n":
            print(name_2, "your result is:", result_2)
            return(result_2)
        elif x == "y": 
            koloda = random.randint(2, 11)
            result_2 += koloda
        else:
            exit()
        print(result_2)
        if result_2 > 21:
            print("You lose!\nGood Bye!\n")
            exit()
if fisrt_oponent() > second_oponent():
    print("First oponent WIN!!!")
else:
    print("Second oponent WIN!!!")
