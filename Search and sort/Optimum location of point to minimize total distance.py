def dist(li,po):
    a=li[0]
    b=li[1]
    c=li[2]
    x=po[0]
    y=po[1]

    cal=a*(x)+b*(y)+c
    if cal<0:
        cal=str(cal)
        cal=cal[1:]
        cal=int(cal)
    n=((a*a)+(b*b))**0.5
    return cal/n

if __name__ == '__main__':
    line=[1,-1,-3]
    point=[[-3, -2],[-1,0],[-1,2],[1,2],[3,4]]
    ans=[]
    for i in range(len(point)):
        ans.append(dist(line,point[i]))
    print(ans)