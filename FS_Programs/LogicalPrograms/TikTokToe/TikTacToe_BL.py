import random
ar=[1,2,3,4,5,6,7,8,9]
def ar_state():
    return ar

def assign(cell):
    ar[cell-1]='O'

def fill(cell):
    ar[cell-1]='X'

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
