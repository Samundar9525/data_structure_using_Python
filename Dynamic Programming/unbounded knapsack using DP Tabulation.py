def display(arr):
    for i in arr:
        for k in i:
            print(k,end="   ")
        print()

def unbound(val,wt,s,n,t):
    for i in range (n+1):
        for j in range (s+1):
            if i==0 or j==0:
                t[i][j]=0
            elif (wt[i-1]<=j):
                t[i][j]=max( val[i-1] + t[i][j-wt[i-1]], t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    display(t)
    return t[n][s]


if __name__ == '__main__':
    val=[10,30,20]
    wt=[5,10,15]
    n=len(val)
    sum=(sum(wt))
    cap=100
    t=[[0 for i in range(cap+1)] for j in range(n+1)]

    print(unbound(val,wt,cap,n,t))