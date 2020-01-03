n=int(input())
ar=[]
distinct=[]
count=0
for i in range(0,n):
    ar.append(int(input()))
''' 
looping through entire array each time to get triplets which sum is zero
'''
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if (ar[i]+ar[j]+ar[k])==0:
                count+=1
                distinct.append([i,j,k])
print(count)
print(distinct)