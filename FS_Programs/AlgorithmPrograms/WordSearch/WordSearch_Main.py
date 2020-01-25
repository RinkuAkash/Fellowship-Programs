import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from WordSearch_BL import Find

word=Input.singleString()
flag=Find(word)
if flag==True:
    print("Found")
else:
    print("Not Found")
