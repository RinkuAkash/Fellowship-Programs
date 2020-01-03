import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from Extended_PrimeNumbers_BL import seiveMethod

if __name__=="__main__":
    n1=Input.singleInt()
    n2=Input.singleInt()
    res=seiveMethod(n1,n2)
    List.linebyline(res)
