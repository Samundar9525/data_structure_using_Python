def sol(arr,n):
    count=0
    index=0

    while(count<n and index<n):
        if arr[count]==count+1:
            count+=1
        else:
            temp=arr[count]
            arr[count]=arr[temp-1]
            arr[temp-1]=temp
            index+=1
    print(arr)


if __name__ == '__main__':
    n=7
    arr=[5,3,6,4,2,1,3]
    sol(arr,n)
