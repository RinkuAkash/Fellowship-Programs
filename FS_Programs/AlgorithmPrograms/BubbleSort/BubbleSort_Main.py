import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from BubbleSort_BL import bubble


ar=Input.multiInt()
ar=bubble(ar)
List.WithOutComma(ar)
