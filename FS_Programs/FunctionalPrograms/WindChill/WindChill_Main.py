import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
from WindChill_BL import Solve

n=Input.commandLine()
print(Solve(float(n[1]),float(n[2])))
