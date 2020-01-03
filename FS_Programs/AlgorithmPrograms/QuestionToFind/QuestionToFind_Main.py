from QuestionToFind_BL import Find
import sys

if __name__=="__main__":
    N=int(sys.argv[1])
    print("Guess a number between 0 and {0}".format(N-1))
    intermediate,final=Find(N)
    print("Intermediate number is {0} and final number is {1}".format(intermediate,final))


