def sol(arr,n):
    di={}
    for i in arr:
        if i not in di:
            di[i]=1
        else:
            di[i]+=1
    ar1=[]
    ar2=[]
    for key,val in di.items():
        if val==1:
            ar1.append(key)
        else:
            for i in range (val):
                ar2.append(key)
    # print(ar1)
    # print(ar2)
    var1=len(ar1)
    var2=len(ar2)
    if var1>n:
        for i in range (n):
            ar1.pop()
        return len(set(ar1))+len(set(ar2))
    else:
        n=n-var1
        for i in range (n):
            ar2.pop()
        return len(set(ar2))

if __name__ == '__main__':
    m=3
    arr=[1,2,5,6,6,5]
    print(sol(arr,m))