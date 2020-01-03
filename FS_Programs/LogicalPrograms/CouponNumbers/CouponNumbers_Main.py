import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from CouponNumbers_BL import Solve

N=Input.singleInt()
distinct_set,count=Solve(N)
print(distinct_set)
print("Total random numbers needed to get distinct numbers are : {0}".format(count))
