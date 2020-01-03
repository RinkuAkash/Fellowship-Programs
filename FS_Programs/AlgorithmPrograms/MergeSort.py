def MergeSort(ar):
    if len(ar)>1:
        mid=len(ar)//2
        L=ar[:mid]
        R=ar[mid:]
        MergeSort(L)
        MergeSort(R)
        i=0
        j=0
        k=0
        while(i<len(L) and j<len(R)):
            if L[i]<R[j]:
                ar[k]=L[i]
                i+=1
            else:
                ar[k]=R[j]
                j+=1
            k+=1
        while(i<len(L)):
            ar[k]=L[i]
            i+=1
            k+=1
        while(j<len(R)):
            ar[k]=R[j]
            j+=1
            k+=1
ar=list(map(int,input().split()))
MergeSort(ar)
print(ar)

