def insertion(ar):
    for i in range(1,len(ar)):
        key=ar[i]
        j=i-1
        while(j>=0 and ar[j]>key):
            ar[j+1]=ar[j]
            j-=1
        ar[j+1]=key
    return ar
