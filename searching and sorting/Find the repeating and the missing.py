def sol( arr, n):
    te = [-1] * n
    bi = 0
    for i in range(n):
        if te[arr[i]-1]!=-1:
            rep=arr[i]
        te[arr[i] - 1] = arr[i]

    for i in range(n):
        if te[i]==-1:
            miss=i+1

    print("repeated : ",rep,'missing',miss)


def optimisedsol(arr,n):
    indx=0
    count=0

    while(indx<n and count<n):
        if arr[count]==arr[arr[count]-1]:
            count+=1
            continue

        if arr[count]==count+1:
            count+=1
        else:
            temp=arr[count]
            arr[count],arr[temp-1]=arr[temp-1],arr[count]
            indx+=1
    for i in range (n):
        if arr[i]!=i+1:
            print('repeated : ',arr[i],'Missing',i+1)






if __name__ == '__main__':
    n=5
    arr=[5,3,2,1,3]
    (sol(arr,n))
    (optimisedsol(arr,n))