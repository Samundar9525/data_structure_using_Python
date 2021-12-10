def heapify(arr, n, indx):
    small = indx
    l = 2 * indx + 1
    r = 2 * indx + 2

    if l < n and arr[l] < arr[small]:
        small = l
    if r < n and arr[r] < arr[small]:
        small = r
    if small != indx:
        arr[small], arr[indx] = arr[indx], arr[small]
        heapify(arr, n, small)

if __name__ == '__main__':
    arr=[6,7,3,9,8,2,4,1,5]
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,len(arr),i)


    print(arr)
