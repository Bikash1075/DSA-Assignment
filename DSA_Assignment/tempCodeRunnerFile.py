def rev_arr(arr,n):
    for i in range(n//2):
        arr[i],arr[n-i]=arr[n-i],arr[i]
    print(arr)
arr=[14,25,87,69,36,52,45]
n=len(arr)
rev_arr(arr,n)