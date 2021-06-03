def display (arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

def countsubset(arr,n,k):
    for i in range(1,n+1):
        for j in range (1,k+1):
            if (arr[i-1]<=j and arr[i-1]>0):
                t[i][j]=t[i-1][j]+t[i-1][j//arr[i-1]]+1
            else:
                t[i][j] = t[i - 1][j]

    return t[n][k]


if __name__ == '__main__':
    arr=[1,2,3,4]
    k=5        #output 11 anan chhaiye
    n=len(arr)
    t=[[0 for i in range (k+1)] for j in range (n+1)]
    print(countsubset(arr,n,k))
    display(t)