import sys
sys.argv # sys.argv takes arguments from commandlines 
n=int(sys.argv[1])
if (0<=n<31):
    for i in range(0,n):
        print(pow(2,i))