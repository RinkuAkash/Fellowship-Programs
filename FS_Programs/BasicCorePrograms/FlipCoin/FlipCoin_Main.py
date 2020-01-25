import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input

from FlipCoin_BL import Find

n=Input.singleInt()
head,tail=Find(n)
print("percentage of head  {0}%".format((head/n)*100))
print("percentage of tail {0}%".format((tail/n)*100))
