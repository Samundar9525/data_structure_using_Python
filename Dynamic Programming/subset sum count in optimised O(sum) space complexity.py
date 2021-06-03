def subsetcount(arr,sum,n,t):

    for i in range (n+1):
        for j in range(sum+1):
            if j == 0:
                t[i % 2][j] = True
            elif i==0:
                t[i%2][j]=False
            #------------   code ko if else me likhna compulsary hai only if nahi chalega ---------
            # --------------Code ko uppar niche rakhne par data galt ata hai-------------
            # if i==0:
            #     t[i % 2][j]=False
            # elif j==0:
            #     t[i % 2][j]=True
            # ---------------------------
            elif arr[i-1]>j:
                t[i%2][j]=t[(i+ 1)%2][j]
            else:
                t[i % 2][j] =t[(i+1)%2][j-arr[i-1]] + t[(i+1)%2][j]
        display(t)
        print("-------------------")
    return t[n%2][sum]



def display (arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()



if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    sum = 6
    n = len(arr)
    t = [[False for i in range(sum + 1)] for j in range(2)]
    print(subsetcount(arr, sum, n, t))