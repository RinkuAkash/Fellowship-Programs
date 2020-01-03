import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
from Distance_BL import Find

n=Input.commandLine()
print(Find(int(n[1]),int(n[2])))
