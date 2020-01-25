import math
def Solve(a,b,c):
    delta=pow(b,2)-4*a*c
    root1=(-b+math.sqrt(delta))//2*a
    root2=(-b-math.sqrt(delta))//2*a
    return root1,root2
