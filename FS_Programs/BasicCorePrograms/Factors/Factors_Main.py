import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from Factors_BL import Factors

n=Input.singleInt()
ar=Factors(n)
List.linebyline(ar)
