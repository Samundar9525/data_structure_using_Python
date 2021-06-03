def mergesort(arr, low, high):
    inv = 0
    if low >= high:
        return 0
    mid = (low + high) // 2
    inv += mergesort(arr, low, mid)
    inv += mergesort(arr, mid + 1, high)
    inv += merge(arr, low, mid, high)
    return inv


def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = low
    inv = 0
    brr = [0] * n
    while (i <= mid and j <= high):
        if arr[i] <= arr[j]:
            brr[k] = arr[i]
            i += 1
            k += 1
        else:
            inv += (mid - i + 1)
            brr[k] = arr[j]
            j += 1
            k += 1

    while (i <= mid):
        brr[k] = arr[i]
        i += 1
        k += 1
    while (j <= high):
        brr[k] = arr[j]
        k += 1
        j += 1

    for i in range(low, high + 1):
        arr[i] = brr[i]
    return inv

if __name__ == '__main__':
    arr=[4,6,1,7,3,2,5]
    arr=[2,4,1,3,5]
    print(arr)
    n=len(arr)
    print(mergesort(arr,0,n-1))
    print(arr)

