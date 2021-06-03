

def mergesort(arr,c):
    if len(arr) <= 1:
        return 0

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    mergesort(left,c)
    mergesort(right,c)
    #yahan fun call hatakar direct apply karwaye hai

    i = 0
    k = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            c+=((len(left)//2)-i+1)
        k += 1

    while (i < len(left)):
        arr[k] = left[i]
        i += 1
        k += 1
    while (j < len(right)):
        arr[k] = right[j]
        j += 1
        k += 1
    return c


if __name__ == '__main__':
    # arr=[2,4,5,6,1,9,3,7,8]
    # arr=[2,4,1,3,5]
    # arr=[1,2,3,4,5]
    arr=[5,4,3,2,1]
    c=0
    print(mergesort(arr,c))
    print(arr)