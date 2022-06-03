#Snanke Water Gun game or Rock Paper Scissors
import random

def gameWin(comp,you):
    #if two selected values are equal
    if comp==you:
        return None
    #check for all possibilities of computer's choose s
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    #check for all possibilities of computer's choose w
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    #check for all possibilities of computer's choose s
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True


randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("Your's Turn: Snake(s),Water(w) or Gun(g) \n")
a=gameWin(comp,you)
print(f"Comp Choose {comp}")
print(f"You Choose {you}")
if a==None:
    print("The game is a tie")
elif a:
    print("You won this game")
else:
    print("You lost this game")
