def naivearrange(arr,n):
    temp=[0]*n
    for i in range (n):
        temp[arr[i]]=i
    return temp

def optimisedarrange(arr,n):
    for i in range (n):
        arr[arr[i] % n] = arr[arr[i] % n] + i * n
    for i in range (n):
        arr[i]=arr[i]//n


if __name__ == '__main__':
    arr = [2, 0, 4, 1, 3]
    n=len(arr)
    print(naivearrange(arr,n))
    print(arr)
    optimisedarrange(arr,n)
    print(arr)