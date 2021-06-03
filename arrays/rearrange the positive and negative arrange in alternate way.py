
def sol(a,n):
    b=[0]*(n)
    k=0
    l=1
    for i in range(n):
        if i%2==0:
            if a[i]>0 and k<n:
                b[k]=a[i]
                k+=2
            else:
                if l<n:
                    b[l] = a[i]
                    l += 2
        else:
            if a[i]<0 and  l<n:
                b[l]=a[i]
                l+=2
            else:
                if k <n:
                    b[k] = a[i]
                    k += 2
    # for i in range (n):
    #     a[i]=b[i]
    while k<n:
        b[k] = a[i]
        k += 1
    while(l<n):
        b[l] = a[i]
        l += 1
    print(b)
if __name__ == '__main__':
    arr=[9 ,4 ,-2, -1, 5, 0, -5, -3, 2,2,4]
    n=len(arr)
    # arr.insert(0,0)
    sol(arr,n)
    # print(arr)