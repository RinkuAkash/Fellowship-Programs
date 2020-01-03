import math #math library is imported to use square root and ceil method
n=int(input())
temp=n
if n%2==0: #checking whether given number is divisible by 2
    while(n%2==0): #Divide the number by 2
        n=n/2
    print(2)
for i in range(3,(math.ceil(math.sqrt(temp)))+2,2):#looping and dividing with odd numbers 
    if n%i==0:
        while(n%i==0):#diving number with prime number unitl prime multiples
            n=n/i
        print(i)