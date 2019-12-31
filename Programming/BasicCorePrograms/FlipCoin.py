import random
n=int(input())#Taking input of no. of times to flip
head=0
tail=0
for i in range(0,n):
    flip=random.uniform(0,1)#random.uniform generate random number within given range
    if flip>0.5:
        head+=1
    else:
        tail+=1
print("Heads %{0:.2f}".format((head/n)*100))
print("Tails %{0:.2f}".format((tail/n)*100))