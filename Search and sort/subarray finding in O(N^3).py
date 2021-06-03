def sol(arr,n):
    ans=[]
    for i in range (n):
        for j in range (i,n):
            t=[]
            for k in range (i,j+1):
                t.append(arr[k])
            ans.append(t)
    return ans

if __name__ == '__main__':
    arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
    # arr=[1,2,3]
    n=len(arr)
    br=(sol(arr,n))
    # for i in br:
    #     print(i) #debug 1
    for i in br:
        if sum(i)==0:
            print(i)
