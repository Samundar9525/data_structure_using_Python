def palindromecount(x,y,n,m,t):
    for i in range (1,n+1):
        for j in range (m+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t[n][m]

def palindromeprint(x,y,n,m,t):
    i=n
    j=m
    res=""

    while(i>0 and j>0):
        if x[i-1]==y[j-1]:
            res=res+x[i-1]
            i=i-1
            j=j-1
        else:
            if (t[i-1][j] > t[i][j-1]):
                i=i-1
            else:
                j=j-1
    return res


if __name__ == '__main__':
    x='agbcba'
    y=x[::-1]

    n=len(x)
    m=n

    t=[[ 0 for i in range (n+1)] for j in range(m+1)]
    print("count of len of palindrome   : ",palindromecount(x,y,n,m,t))
    print("palindrome string \t\t\t :",palindromeprint(x,y,n,m,t))