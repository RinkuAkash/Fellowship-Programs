import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
from Quadratic_BL import Solve

a=Input.singleInt()
b=Input.singleInt()
c=Input.singleInt()
print(Solve(a,b,c))
