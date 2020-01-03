def bubble(ar):
    for i in range(0,len(ar)):
        for j in range(0,len(ar)-1):
            if ar[j+1]<ar[j]:
                ar[j],ar[j+1]=ar[j+1],ar[j]
    return ar
