import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

from SumOfThree_BL import Solve
import Input,List

n=Input.singleInt()
ar=Input.multiInt()
count,distinct=Solve(n,ar)
print(count)
List.WithOutComma(distinct)
