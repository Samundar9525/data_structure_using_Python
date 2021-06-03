def issubset(arr,sum,n):
    if sum==0:
        return 1

    if n==0 and sum!=0:
        return False

    if arr[n-1]>sum:
        return issubset(arr,sum,n-1)
    else:
        return issubset(arr,sum-arr[n-1],n-1) + issubset(arr,sum,n-1)


if __name__ == '__main__':
    arr=[1,2,3,4,5,6,7]
    sum=17

    n=len(arr)
    print(issubset(arr,sum,n))