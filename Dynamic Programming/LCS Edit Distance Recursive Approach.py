
def editdist(x,y,n,m):
    if m==0:
        return n

    if n==0:
        return m

    if x[n-1]==y[m-1]:
        temp=editdist(x,y,n-1,m-1)
        return temp
    else:
        temp=min(editdist(x,y,n-1,m),editdist(x,y,n,m-1),editdist(x,y,n-1,m-1))
        return temp+1

if __name__ == '__main__':
    x="sunday"
    y="saturday"
    n=len(x)
    m=len(y)
    print(editdist(x,y,n,m))