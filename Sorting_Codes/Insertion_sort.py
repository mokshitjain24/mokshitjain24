def insertion(arr,n):
    for i in range(n):
        j=i
        while(j>0 and arr[j-1]>arr[j]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j-=1
    return arr


a = [1,42,53,2,56,3,11,25]
n = len(a)
print(insertion(a,n))