

def lcscount(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    if t[n][m]!=-1:
        return t[n][m]

    if x[n-1]==y[m-1]:
        t[n][m]=1+lcscount(x,y,n-1,m-1,t)
    else:
        t[n][m]=max(lcscount(x,y,n,m-1,t),lcscount(x,y,n-1,m,t))
    return t[n][m]




if __name__ == '__main__':
    x="madeutyur"
    y="medur"
    n=len(x)
    m=len(y)
    t=[[-1 for i in range(m+1)] for j in range (n+1)]
    print(lcscount(x,y,n,m,t))