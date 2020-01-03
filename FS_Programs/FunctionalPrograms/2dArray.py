M=int(input())
N=int(input())
ar=[]
for i in range(0,M):
    ar.append([])
for i in range(0,M):
    for j in range(0,N):
        val=input()
        '''
        Checking input value type using try/except
        '''
        try:
            ar[i].append(int(val))
        except ValueError:
            try:
                ar[i].append(float(val))
            except ValueError:
                p=set(val)
                s={'0','1'}
                if s==p or p=={'0'} or p=={'1'}:
                    ar[i].append(bin(int(val,2)))
                elif val in ['true','True']:
                    ar[i].append(True)
                elif val in ['false','False']:
                    ar[i].append(False)
                else:
                    ar[i].append(val)
print(ar)