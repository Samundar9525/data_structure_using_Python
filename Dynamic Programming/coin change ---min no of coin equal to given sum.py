def count(arr,n):
    t=[0]*(n+1)

    for i in range (1,n+1):
        t[i]=-999999
        for j in range(len(arr)):
            if i-arr[j]>=0 :
                t[i]=max(t[i-arr[j]]+1,t[i])
    print(t)
    return t[n]


if __name__ == '__main__':
    arr=[1,2,1]
    sum=4
    print("kam se kam itna maal chhaiye : ",count(arr,sum))