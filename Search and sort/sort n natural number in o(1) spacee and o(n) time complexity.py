def sol(arr,n):
    index=0
    count=0

    while(index<n and count<n):
        if arr[count]==count+1:
            count+=1
        else:
            tem=arr[count]
            # arr[count]=arr[tem-1]
            # arr[tem-1]=tem
            arr[count],arr[tem-1]=arr[tem-1],arr[count]

            index+=1
    return(arr)


if __name__ == '__main__':
    n=7
    ar=[5,6,4,7,2,1,3]

    art=sol(ar,n)
    print()
    print(sol(art,n))