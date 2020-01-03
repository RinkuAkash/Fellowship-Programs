from primeNumbers_BL import seiveMethod

if __name__=="__main__":
    n1=int(input())
    n2=int(input())
    ar=seiveMethod(n1,n2)
    for i in range(n1,n2+1):
        if ar[i]==True:
            print(i,end=" ")
