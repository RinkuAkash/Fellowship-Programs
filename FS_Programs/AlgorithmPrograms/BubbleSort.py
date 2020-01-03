ar=list(map(int,input().split()))
for i in range(0,len(ar)):
    for j in range(0,len(ar)-i-1):
        if ar[j]>ar[j+1]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
print(ar)
