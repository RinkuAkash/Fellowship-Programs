import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from InsertionSort_BL import insertion

ar=Input.multiInt()
ar=insertion(ar)
List.WithOutComma(ar)
