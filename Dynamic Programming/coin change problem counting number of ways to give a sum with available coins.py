def subsetcount(arr,n,sum,t):
    for i in range (n+1):
        for j in range (sum+1):
            if j==0:
                t[i % 2][j]=1
            elif i==0:
                t[i % 2][j] = 0
            elif arr[i-1]<=j:
                t[i % 2][j] = t[i % 2][j-arr[i-1]] + t[(i+1) % 2][j]
            else:
                t[i % 2][j] =t[(i + 1) % 2][j]
    return  t[n % 2][sum]


def coin(arr,total):
    n=len(arr)
    sum=total
    t=[[0 for i in range (sum+1)] for j in range (2)]
    print("Total possible ways: ",subsetcount(arr,n,sum,t))



if __name__ == '__main__':
    arr=[2, 3, 5, 6]
    Total=10
    coin(arr,Total)