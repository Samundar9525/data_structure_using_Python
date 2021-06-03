def lcscount(x,y,n,m):
    if n==0 or m==0:
        return 0
    if x[n-1]==y[m-1]:
        return 1+lcscount(x,y,n-1,m-1)
    else:
        return max(lcscount(x,y,n-1,m),lcscount(x,y,n,m-1))

if __name__ == '__main__':
    x = "madeutyur"
    y = "medur"
    n=len(x)
    m=len(y)
    print(lcscount(x,y,n,m))
#iska output 3 ana chhaiye