def seg(arr):
    n=len(arr)
    no_of_zeros=0
    for i in range (n):
        if arr[i]==0:
            no_of_zeros+=1
            arr[i]=1
    for j in range (no_of_zeros):
        arr[j]=0
    return  arr




if __name__ == '__main__':
    arr = [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]
    print(arr)
    seg(arr)
    print(arr)