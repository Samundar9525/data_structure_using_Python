def naiveright(arr,k):
    n=len(arr)
    for p in range(k):
        temp=arr[n-1]
        for i in range (n-1,0,-1):
            arr[i]=arr[i-1]

        arr[0]=temp
    print(arr)

def naiveleft(arr,k):
    n=len(arr)
    for p in range (k):
        temp=arr[0]
        for i in range (n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    print(arr)

def reverse(arr,i,j):
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr

def rotateright(arr,k):
    n=len(arr)
    reverse(arr,len(arr)-k,n-1)
    reverse(arr,0,(len(arr)-1)-k)
    reverse(arr,0,len(arr)-1)
    print(arr)

def rotateleft(arr,k):
    n=len(arr)
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,len(arr)-1)
    print(arr)

if __name__ == '__main__':
    arr = [1, 2, 3, 4,5]
    k=2
    print("\n\n\t\t\t\t\tORIGINAL ARRAY :              ",arr,"\t\t\t\t\t\tVALUE of k   :     ",k,"\n\n")
    print("-------------------------------right rotation using naive------------------------------------------------")
    naiveright(arr, k)  # naive approch
    print("-------------------------------right rotation using optimised way------------------------------------------------")
    brr = [1, 2, 3, 4, 5]
    rotateright(brr, k)  # optimised function call
    print("\n \t\t\t\t\t#######################################################################\n")
    print("-------------------------------Left rotation using naive------------------------------------------------")
    crr = [1, 2, 3, 4, 5]
    naiveleft(crr,k)
    print("-------------------------------Left rotation using optimised------------------------------------------------")
    drr = [1, 2, 3, 4, 5]
    rotateleft(drr,k)