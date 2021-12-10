def sol(arr,n):
    prev = 1
    for i in range(len(arr)):
        prev = i - 1
        if (n <= arr[i][0]):
            break
    for i in arr[prev + 1]:
        if n == i:
            return True
    for i in arr[prev]:
        if n == i:
            return True
    return False



if __name__ == '__main__':
    # arr=[[1,3,5,7],
    #      [10,11,16,20],
    #      [23,30,34,60]]

    arr=[[1],[3]]
    n=1

    print(sol(arr,n))
