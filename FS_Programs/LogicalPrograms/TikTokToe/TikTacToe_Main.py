import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from TikTacToe_BL import *

game=True

while(game):
    printBoard()
    print("Enter cell number")
    cell=int(input())
    ar=ar_state()
    if ar[cell-1]!='X' or ar[cell-1]!='O':
        fill(cell)
        ret_player=check_player()
        ar=ar_state()
        ret_computer=check_computer()
        ar=ar_state()
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
             ar=ar_state()
             while(ar[computer_cell-1] is not computer_cell):
                 computer_cell=random.randint(1,9)
             assign(computer_cell)
             ret_computer=check_computer()
             if ret_computer:
                 print("Try next time")
                 game=False
    else:
        print("Enter valid cell number")

