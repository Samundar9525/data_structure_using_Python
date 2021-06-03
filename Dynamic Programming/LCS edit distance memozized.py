def editdist(x,y,n,m):
    if m==0:
        return n
    if n==0:
        return m
    if t[n][m]!=-1:
        return t[n][m]
    if x[n-1]==y[m-1]:
        t[n][m]=editdist(x,y,n-1,m-1)

    else:
        t[n][m]=1+min(editdist(x,y,n-1,m),editdist(x,y,n,m-1),editdist(x,y,n-1,m-1))
    return t[n][m]


if __name__ == '__main__':
    x="sunday"
    y="saturday"
    n=len(x)
    m=len(y)

    t=[[-1 for i in range (m+1)] for j in range (n+1)]

    print(editdist(x, y, n, m))