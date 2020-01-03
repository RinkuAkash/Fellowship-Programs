import random
ar=[1,2,3,4,5,6,7,8,9]

def check(cell):
    if 1<=cell<=9 and ar[cell-1]==cell-1:
        return True
    else:
        return False

def check_computer():
    if ar[0]==ar[1]==ar[2]=='O':
        return True
    elif ar[3]==ar[4]==ar[5]=='O':
        return True
    elif ar[6]==ar[7]==ar[8]=='O':
        return True
    elif ar[0]==ar[3]==ar[6]=='O':
        return True
    elif ar[1]==ar[4]==ar[7]=='O':
        return True
    elif ar[2]==ar[5]==ar[8]=='O':
        return True
    elif ar[0]==ar[4]==ar[8]=='O':
        return True
    elif ar[2]==ar[4]==ar[6]=='O':
        return True
    else:
        return False

def check_player():
    if ar[0]==ar[1]==ar[2]=='X':
        return True
    elif ar[3]==ar[4]==ar[5]=='X':
        return True
    elif ar[6]==ar[7]==ar[8]=='X':
        return True
    elif ar[0]==ar[3]==ar[6]=='X':
        return True
    elif ar[1]==ar[4]==ar[7]=='X':
        return True
    elif ar[2]==ar[5]==ar[8]=='X':
        return True
    elif ar[0]==ar[4]==ar[8]=='X':
        return True
    elif ar[2]==ar[4]==ar[6]=='X':
        return True
    else:
        return False

def printBoard():
    print(ar[0],"|",ar[1],"|",ar[2])
    print("_   _   _")
    print(ar[3],"|",ar[4],"|",ar[5])
    print("_   _   _")
    print(ar[6],"|",ar[7],"|",ar[8])
game=True
while(game):
    printBoard()
    print("Enter cell number")
    cell=int(input())
    if ar[cell-1]!='X' or ar[cell-1]!='O':
        ar[cell-1]='X'
        ret_player=check_player()
        ret_computer=check_computer()
        if ret_player and ret_computer:
            print("It's a tie")
            game=False
        elif ret_computer:
            print("Try next time")
            game=False
        elif ret_player:
            print("Congratulations, you won")
            game=False
        else:
             computer_cell=random.randint(1,9)
             while(ar[computer_cell-1] is not computer_cell):
                 computer_cell=random.randint(1,9)
             ar[computer_cell-1]='O'
             ret_computer=check_computer()
             if ret_computer:
                 print("Try next time")
                 game=False
    else:
        print("Enter valid cell number")

