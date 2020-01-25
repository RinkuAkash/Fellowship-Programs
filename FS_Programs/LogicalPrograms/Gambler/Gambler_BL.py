import random

def Solve(stake,goal,no_of_times):
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
    return win,loss
