def selection(arr,n):
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

a = [0,4,1,68,532,683,12]
n = len(a)
print(selection(a,n))
    

