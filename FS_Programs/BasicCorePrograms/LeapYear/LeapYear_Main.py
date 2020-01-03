import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from LeapYear_BL import Find

year=Input.singleInt()
if Find(year):
    print("Leap Year")
else:
    print("Not a Leap Year")
