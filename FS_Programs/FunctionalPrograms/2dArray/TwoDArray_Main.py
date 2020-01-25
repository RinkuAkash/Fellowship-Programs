import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

from TwoDArray_BL import TwoD

import Input,List

M=Input.singleInt()
N=Input.singleInt()
ar=TwoD(M,N)
List.linebyline(ar)
