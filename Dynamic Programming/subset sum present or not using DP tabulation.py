def subset(arr,sum,n,t):
     #----------------------------------inititalizing the 2-d array
    for i in range(1,sum+1):
        t[0][i]=False

    for j in range(n+1):
        t[j][0]=True
    #-----------------------------------dispaly(t)

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
        dispaly(t)
        print()
    return t[n][sum]


def dispaly(ar):
    for i in range(len(ar[0])):
        print("  ",i,end="  ")
    print()
    k=-1
    for i in ar:
        k += 1
        print(k,end=" |")
        for j in i:
            print(j,end=" ")
        print("")



if __name__ == '__main__':
    arr=[1,2,3,4,5,6]
    sum=6
    n=len(arr)
    t=[[False for i in range(sum+1)] for j in range(n+1)]
    print(subset(arr,sum,n,t))