def sump(arr,n,k):
    dic={}
    for i in range (n):
        if arr[i] not in dic:
            dic[arr[i]]=1
        else:
            dic[arr[i]]+=1
    print(dic)
    c=0

    for i in range (n):
        if k-arr[i] in dic:
            # print(c,dic[k-arr[i]])
            c+=dic[k-arr[i]]
        if k-arr[i]==arr[i]:
            c-=1
    return c//2

if __name__ == '__main__':
    arr=[1,1,1,1]
    arr=[1, 5, 7, 1,4,2,6]
    k=6
    print(sump(arr,len(arr),k))