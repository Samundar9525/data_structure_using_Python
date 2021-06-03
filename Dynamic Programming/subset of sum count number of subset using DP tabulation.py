def subsetcount(arr,sum,n,t):
    for i in range(1,sum+1):
        t[0][i]=0
    for j in range (n+1):
        t[j][0]=1

    for i in range(1,n+1):
        for j in range (1,sum+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j-arr[i-1]]+t[i-1][j]
        display(t)
        print("-------------------")

    return t[n][sum]


def display (arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

if __name__=='__main__':
    arr=[1,2,3,4,5,6]
    sum=6
    n=len(arr)
    t=[[0 for i in range (sum+1)] for j in range(n+1)]
    print(subsetcount(arr,sum,n,t))