import random
N=int(input())
max_limit=int(10**(N))
min_limit=int(10**(N-1))
distinct_set=set()
count=0
while(len(distinct_set)!=N):
    New_no=random.randint(min_limit,max_limit)
    if New_no not in distinct_set:
        distinct_set.add(New_no)
    count+=1
print("Total random numbers need to have all distinct numbers are: %d"%count)