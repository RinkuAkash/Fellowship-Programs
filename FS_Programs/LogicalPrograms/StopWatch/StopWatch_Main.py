import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from StopWatch_BL import start,stop

print("Enter 1 to start stopwatch")
key=Input.singleInt()
if key==1:
    start=start()
    print("Enter 0 to stop stopwatch")
    key=Input.singleInt()
    if key==0:
        print("Elapsed time is : ",stop(start))
