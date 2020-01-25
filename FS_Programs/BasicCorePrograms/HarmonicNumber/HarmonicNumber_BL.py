def Find(n):
    H=1  #Assigning harmonic number with 1
    for i in range(2,n+1): # generating nth harmonic number
        H+=1/i
    return H
