year=int(input())
'''
we can find leap by dividing with 4,100 and 400
'''
if len(str(year))==4: #Checking the length of input integer
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")
else:
    print("Invalid input")