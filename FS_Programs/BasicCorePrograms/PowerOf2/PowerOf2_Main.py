import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input,List
from PowerOf2_BL import Find

n=Input.commandLine()
ar=Find(int(n[1]))
List.linebyline(ar)
