'''
we can find leap by dividing with 4,100 and 400
'''
def Find(year):
    if len(str(year))==4: #Checking the length of input integer
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False
