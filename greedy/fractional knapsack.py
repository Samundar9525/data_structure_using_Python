def sol(di,w):
    res=0
    for i in range(len(di)):
        if w-di[i][1]>0:
            w=w-di[i][1]
            res+=di[i][0]
        else:
            p=(w/di[i][1])*di[i][0]
            res+=p
            break
    return (res)




if __name__ == '__main__':

    val = [60,100,120]
    wt =  [10,20,30]
    di=[]
    w=50
    for i in range(len(val)):
        di.append([val[i],wt[i],val[i]/wt[i]])
    print(di)
    d=sorted(di, key=lambda a:a[2],reverse=True)
    print(d)
    print(sol(d,w))