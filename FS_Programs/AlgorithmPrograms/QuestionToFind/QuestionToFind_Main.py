import sys
sys.path.append("/home/rinku/Desktop/bridgelabz/FS_Programs/Utility")

import Input
from QuestionToFind_BL import Find


if __name__=="__main__":
    N=Input.commandLine()
    print("Guess a number between 0 and {0}".format(int(N[1])-1))
    intermediate,final=Find(int(N[1]))
    print("Intermediate number is {0} and final number is {1}".format(intermediate,final))


