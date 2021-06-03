# note isme pure unbouded eknapsack ka conceot lagega
def rod (len,price,n,s,t):
    for i in range (n+1):
        for j in range (s+1):
            if i==0 or j==0 :
                t[i][j]=0
            elif(len[i-1]<=j):
                t[i][j]=max(price[i-1]+t[i][j-len[i-1]],t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[n][s]


def rodoptimised(len,price,n,s,t):
    for i in range (n+1):
        for j in range(s+1):
            if i==0 or j==0:
                t[i % 2][j]=0
            elif(len[i-1]<=j):
                t[i % 2][j]=max(t[i % 2][j-len[i-1]]+price[i-1],t[(i + 1) % 2][j])
            else:
                t[i % 2][j]=t[(i + 1) % 2][j]
    return t[n % 2][j]

if __name__ == '__main__':
#------------- INPUTS  ----------------------------
    N=8
    price=[3 , 5, 8, 9, 10, 17, 17, 20]
#------------------------------------------------
    len=[i for i in range(1,N+1)]
    t=[[0 for i in range (N+1)] for j in range (N+1)]
    print(rod(len,price,N,N,t))
    
    k=[[0 for i in range(N+1)] for j in range (2)]
    print(rodoptimised(len,price,N,N,k))
