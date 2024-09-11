import random
computer_number=random.randint(1,10)
chance=4
def clue():
    if computer_number>5:
        print("hidden number is greater than 5")
    elif computer_number<5:
        print("hidden number is less than 5")

while True:
    my_number=int(input("guess a number: "))
    if my_number==computer_number:
        print("hurray! you gussed it right!")
        break
    if my_number!=computer_number:
        chance=chance-1
        clue2 =input("Do you want any clue? Y/N")
        if clue2=="Y":
            clue()
        print(f"you have {chance} chances left")
        if chance==0:
            print("game over!")
            break