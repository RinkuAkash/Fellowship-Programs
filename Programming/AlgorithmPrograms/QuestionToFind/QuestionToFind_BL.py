def Find(N):
    low=0
    high=N-1
    ar=[]
    while(low<=high):
        if low==high:
            mid=high
            break
        mid=(low+high)//2
        check=int(input("Enter 1 if the number in between {0} and {1} else enter 0\n".format(low,mid)))
        if check==1:
            high=mid
        else:
            low=mid+1
        ar.append(mid)
    return ar[len(ar)//2],mid
