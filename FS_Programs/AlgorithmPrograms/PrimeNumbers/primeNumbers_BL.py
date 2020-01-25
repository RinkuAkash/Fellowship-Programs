
def seiveMethod(min_limit,max_limit):
    ar=[True]*(max_limit+1)
    ar[0]=ar[1]=False
    i=4
    while(i%2==0 and i<=max_limit):
        ar[i]=False
        i+=2
    for i in range(3,max_limit+1,2):
        if ar[i]==True:
            k=i+i
            while(k%i==0 and k<=max_limit):
                ar[k]=False
                k+=i
    return ar
