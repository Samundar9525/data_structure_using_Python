
def display(arr):
    for i in (arr):
        for j in i :
            print(j,end=" ")
        print("")

def editdist(x,y,n,m):
    for i in range (n+1):
        for j in range (m+1):
            if i==0:
                t[i][j]=j
            elif j==0:
                t[i][j]=i 
               
            elif(x[i-1]==y[j-1]):
                t[i][j]=t[i-1][j-1]
            else:
                t[i][j]=1+min(t[i-1][j],t[i][j-1],t[i-1][j-1])
    return t[n][m]


if __name__ == '__main__':
    x="ecfbefdcfca"
    y="badfcbebbf"
    n=len(x)
    m=len(y)

    t=[[0 for i in range (m+1)] for j in range (n+1)]

    print(editdist(x, y, n, m))
    display(t)
