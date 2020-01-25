def Find(n):
    ar=[]
    if (0<=n<31):
        for i in range(0,n):
            ar.append(pow(2,i))
    return ar
