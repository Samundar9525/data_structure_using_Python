def display (t):
    for i in range (len(t)):
        for j in range (len(t[0])):
            print(t[i][j],end=" ")
        print()

def lcscount(x,y,n,m,t):
    for i in range (1,n+1):
        for j in range (m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif(x[i-1]==y[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[n][m]

def scscount(x,y,n,m,t):
    res=(m+n)-lcscount(x,y,n,m,t)
    print("length of superstring is : ",res)
    return "done"

def scsprint(x,y,n,m,t):
    i=n;j=m;res=""
    while(i>0 and j>0):
        if (x[i-1]==y[j-1]):
            res=res+x[i-1]
            i=i-1
            j=j-1
        else:
            if t[i][j-1]>t[i-1][j]:
                res=res+y[j-1]
                j=j-1
            else:
                res=res+x[i-1]
                i=i-1

    print(i,j)
    while(i>0):
        res=res+x[i-1]
        i=i-1
    while(j>0):
        res=res+y[j-1]
        j=j-1
    return res[::-1]


if __name__ == '__main__':
    x="abac"
    y="cab"
    n=len(x)
    m=len(y)

    t=[[ 0 for i in range (m+1)] for j in range (n+1)]
    print("scs funtion initializing :",scscount(x,y,n,m,t))
    print("-------------------------------------")
    print(scsprint(x,y,n,m,t))
