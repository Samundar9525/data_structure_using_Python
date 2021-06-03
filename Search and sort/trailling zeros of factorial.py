def check(mid,n):
    tem=mid
    c=0
    f=5
    y=0
    while(f<=tem):
        print("in check : ",tem,"//","5^",y," = ", "floor|",tem,"//",f,"| =",tem//f)
        c+=tem//f
        f=f*5
        y+=1
    if c>=n:
        return True
    else:
        return False

def fun(n):
    if n==1:
        return 5
    low=0
    high=n*5
    g=0
    while(low<high):
        g+=1
        print("pass :",g)
        mid=(low+high)//2
        print("low :", low, "  high :", high, "  mid :", mid)
        if (check(mid,n)):
            high=mid
        else:
            low=mid+1
    return low

if __name__ == '__main__':
    n=6
    print(fun(n))


