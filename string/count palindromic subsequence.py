def sol(x,n):
    for i in range(n):
        t[i][i]=1

    for i in range (2,n+1):
        for j in range (n):
            k=i+j-1
            if k<n:
                if x[j]==x[k]:
                    t[j][k]=1+(t[j][k-1]+t[j+1][k])
                else:
                    t[j][k]=t[j][k-1]+t[j+1][k]-t[j+1][k-1]
    return t[0][n-1]

# def display(arr):
#     n=len(arr)
#     m=len(arr[0])
#     for i in range(n):
#         for j in range (m):
#             print(arr[i][j],end=' ')
#         print()

if __name__ == '__main__':
    st='abca'
    n=len(st)
    t=[[0 for i in range(n+2)]for j in range (n+2)]
    print(sol(st,n))
    # display(t)