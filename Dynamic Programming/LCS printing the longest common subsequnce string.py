def display(arr):
    for i in range(len(arr)):
        for j in range (len(arr[0])):
            print(arr[i][j],end=" ")
        print()


def lcscount(x,y,n,m,t):
    for i in range (1,n+1):
        for j in range (m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[n][m]

def lcsfind(x,y,n,m,t):
    i=n
    j=m
    res=""
    while(i>0 and j>0):
        if x[i-1]==y[j-1]:
            res+=x[i-1]
            i-=1
            j-=1
        else:
            if t[i][j-1]>t[i-1][j]:
                j-=1
            else:
                i-=1
    return res[::-1]

if __name__ == '__main__':
    x='abcdef'
    y='abfxed'
    n=len(x)
    m=len(y)

    t=[[0 for i in range (m+1)] for j in range (n+1)]

    print(lcscount(x,y,n,m,t))
    display(t)
    print(lcsfind(x,y,n,m,t))