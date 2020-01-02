import random
N=int(input())
distinct_set=set()
count=0
while(len(distinct_set)!=N):
    New_no=random.randint(1,N)
    if New_no not in distinct_set:
        distinct_set.add(New_no)
    count+=1
print(distinct_set)
print("Total random numbers need to have all distinct numbers are: %d"%count)
