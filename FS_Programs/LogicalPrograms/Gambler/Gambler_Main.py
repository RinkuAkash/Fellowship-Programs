import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from Gambler_BL import Solve

stake=Input.singleInt()
goal=Input.singleInt()
no_of_times=Input.singleInt()

win,loss=Solve(stake,goal,no_of_times)
print("No. of wins :%d"%win+" and win/loss percentage is : {0}".format((win*100)/loss)+"%")
