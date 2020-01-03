import random
def Find(n):
    head=0
    tail=0
    for i in range(0,n):
        flip=random.random()#random.random() generate random number within given range
        if flip>0.5:
            head+=1
        else:
            tail+=1
    return head,tail
