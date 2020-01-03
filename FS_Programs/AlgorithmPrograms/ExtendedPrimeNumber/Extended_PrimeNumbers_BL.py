
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
    result=set()
    for i in range(min_limit,max_limit+1):
        if ar[i]==True:
            rev=0
            temp=i
            while(temp!=0):
                rev=rev*10+(temp%10)
                temp=temp//10
            if ar[rev]==True and i==rev:
                result.add(i)
                result.add(rev)
    return result
