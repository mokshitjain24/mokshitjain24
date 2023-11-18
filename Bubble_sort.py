def bubble(arr,n):
    for i in range(n,0,-1):
        swaps = 0
        for j in range(0,i-1):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swaps = 1
        if(swaps==0):
            break; 
    return arr


arr = [1,2,3,4]
n = len(arr)
print(bubble(arr,n))