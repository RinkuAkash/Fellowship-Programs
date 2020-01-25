import random
def Solve(N):
    distinct_set=set()
    count=0
    while(len(distinct_set)!=N):
        New_no=random.randint(1,N)
        if New_no not in distinct_set:
            distinct_set.add(New_no)
        count+=1
    return distinct_set,count
