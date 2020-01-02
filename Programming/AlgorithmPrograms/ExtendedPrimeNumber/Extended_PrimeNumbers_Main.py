from Extended_PrimeNumbers_BL import seiveMethod

if __name__=="__main__":
    n1=int(input())
    n2=int(input())
    res=seiveMethod(n1,n2)
    for i in res:
        print(i)
