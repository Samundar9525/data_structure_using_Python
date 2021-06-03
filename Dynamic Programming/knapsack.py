def display(arr):
    # for j in range(len(arr[0])):
    #     print(j,end='   ')
    # print()
    for i in arr:
        for k in i:
            print(k,end="   ")
        print()



def knapsack(w,wt,val,n):
    k=[[0 for i in range(w+1)] for j in range(n+1)]
    for i in range (n+1):
        for j in range (w+1):
            if i==0 or j==0:
                k[i][j]=0
            elif(wt[i-1]<=j):
                k[i][j]=max(val[i-1]+k[i-1][j-wt[i-1]],k[i-1][j])
                display(k)
                print("---------------------------")
            else:
                k[i][j]=k[i-1][j]
    display(k)
    return k[n][w]



if __name__ == '__main__':
    wt=[1,2,3]
    val=[25,25,40]
    w=3
    n=len(val)
    print("maxm profit is : ",knapsack(w,wt,val,n))


























