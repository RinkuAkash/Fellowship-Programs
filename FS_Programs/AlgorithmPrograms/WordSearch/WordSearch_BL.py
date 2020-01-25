def Find(word):
    f=open("1-1000.txt","r")
    f1=f.readlines()
    ar=[]
    for i in f1:
        ar.append(i.rstrip('\n'))
    ar.sort()

    low=0
    high=len(ar)-1
    flag=False
    while(low<high):
        mid=(low+high)//2
        if ar[mid]==word:
            flag=True
            break
        if ar[mid]>word:
            high=mid-1
        else:
            low=mid+1
    return flag
