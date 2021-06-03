

def inv(arr,n):
    c=0
    for i in range (n):
        for j in range (i,n):
            if arr[i]>arr[j]:
                c+=1
    return c


if __name__ == '__main__':
    arr = [2 ,4 ,1, 3, 5]
    n=len(arr)
    t=[]
    print(inv(arr,n))
