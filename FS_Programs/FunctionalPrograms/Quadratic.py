import math
a=int(input())
b=int(input())
c=int(input())
delta=pow(b,2)-4*a*c
root1=(-b+math.sqrt(delta))//2*a
root2=(-b-math.sqrt(delta))//2*a
print(root1,root2)