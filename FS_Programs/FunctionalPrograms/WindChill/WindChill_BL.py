def Solve(t,v):
    if abs(t)<=50 and 2<abs(v)<=120:
        w=35.74+(0.6125*t)+((0.4275*t)-35.75)*pow(v,0.16)
    return w
