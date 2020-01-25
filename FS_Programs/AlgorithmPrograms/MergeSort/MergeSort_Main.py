import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from MergeSort_BL import Merge

ar=Input.multiInt()
ar=Merge(ar)
List.WithOutComma(ar)
