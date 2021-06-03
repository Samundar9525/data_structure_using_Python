def sor (arr):
    i=0
    j=1
    while(arr[i]>arr[j] and j<len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j+=1

def sol(arr1,arr2,n,m):
    i=0
    j=0
    while(i<n and j<n):
        if arr1[i]>arr2[j]:
            arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            sor(arr2)

    print(arr1)
    print(arr2)


def gapfind(gap):
    if gap%2==0:
        return gap//2
    else:
        return (gap//2) +1



def optisol(arr1,arr2,n,m):
    if (n+m)%2==0:
        gap=(n+m)//2
    else:
        gap=(n+m)//2
        gap+=1
    st=0

    for i in range (n+m-gap):
        pass


    while(gap>1):
        print(gap)



        gap=gapfind(gap)

if __name__ == '__main__':
    arr1=[1, 3, 5, 7]
    arr2=[0, 2, 6, 8, 9]
    sol(arr1,arr2,len(arr1),len(arr2))
    optisol(arr1,arr2,len(arr1),len(arr2))