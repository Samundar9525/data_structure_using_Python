def lcscount(x,y,n,m,t):
    for i in range(1,n+1):
        for j in range (m+1):
            if i==0 or j==0:   # ye base case hai isko hatane pe galat ans ata hai
                t[i][j]=0      # hence do not ignore this
            elif (x[i-1]==y[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j] , t[i][j-1])
    return t[n][m]

if __name__ == '__main__':
    x="abcdef"
    y="fecda"
    n=len(x)
    m=len(y)
    t=[[0 for i in range (m+1)] for j in range (n+1)]
    print(lcscount(x,y,n,m,t))