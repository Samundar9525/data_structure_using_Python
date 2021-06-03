def lcscount(x,y,n,m,t):
    for i in range(1,n+1):
        for j in range(m+1):
            if i==0 or j==0:
                t[i][j]=0
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[n][m]

def longest(x,y,n,m,t):
    res=-99999
    for i in range(1,n+1):
        for j in range (m+1):
            if i ==0 or j==0:
                t[i][j]=0

            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
                res = max(res, t[i][j])
            else:
                t[i][j]=0
    return res


if __name__ == '__main__':
    x="samundar"
    y="etersfsdftryrttgsrysamfghtsgghgfhrytut"
    n=len(x)
    m=len(y)

    t=[[0 for i in range (m+1)] for j in range (n+1)]

    print("Number of the LCS is : ",lcscount(x,y,n,m,t))

    print("Length of longest substring : ",longest(x,y,n,m,t))
