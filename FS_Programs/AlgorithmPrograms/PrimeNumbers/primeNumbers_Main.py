import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from primeNumbers_BL import seiveMethod

if __name__=="__main__":
    n1=Input.singleInt()
    n2=Input.singleInt()
    ar=seiveMethod(n1,n2)
    for i in range(n1,n2+1):
        if ar[i]==True:
            print(i,end=" ")
