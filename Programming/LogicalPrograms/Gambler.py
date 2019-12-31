import random
stake=int(input())
goal=int(input())
no_of_times=int(input())
win=0
loss=0
for i in range(0,no_of_times):
    if stake==goal:
        break
    if random.random() > 0.5:
        stake+=1
        win+=1
    else:
        stake-=1
        loss+=1
print("No. of wins: %d"%win+" and Win/Loss percentage: {0}".format(win*100/loss)+"%")
