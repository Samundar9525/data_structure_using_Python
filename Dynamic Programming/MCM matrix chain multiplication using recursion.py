def solve(arr,i,j):
    if i>=j:
        return 0
    res=999999
    for k in range (i,j):
        temp=solve(arr,i,k)+solve(arr,k+1,j)+(arr[i-1]*arr[k]*arr[j])
        if temp<res:
            res=temp
    return res


if __name__ == '__main__':
    arr=[40,20,30,10,30]
    arr2=[10,20,30,40,30]
    arr3=[10,20,30]
    print(arr,"-------->  ",solve(arr,1,len(arr)-1))
    print(arr2,"-------->  ",solve(arr2,1,len(arr2)-1))
    print(arr3,"\t\t\t------> ",solve(arr3,1,len(arr3)-1))