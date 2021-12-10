#for heap sort implement the max heap

def heapify(arr,n,indx):
    largest=indx
    l=2*indx+1
    r=2*indx+2

    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=indx:
        arr[largest],arr[indx]=arr[indx],arr[largest]
        heapify(arr,n,largest)

def minheapify(arr,n,indx):
    small=indx
    l=2*indx+1
    r=2*indx+2

    if l<n and arr[l]<arr[small]:
        small=l
    if r<n and arr[r]<arr[small]:
        small=r
    if small!=indx:
        arr[small],arr[indx]=arr[indx],arr[small]
        minheapify(arr,n,indx)


if __name__ == '__main__':
    arr=[2,5,9,7,6,8,1]
    n=len(arr)
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr,n,i)
    print(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
    print(arr)

    print(arr[::-1])