temp=[]
def permutation(st,count,res,start):
    if start==len(arr):
        temp.append(res)
        for i in res:
            print(i,end="")
        print(end=" ")
        return

    for i in range(len(st)):
        if count[i]==0:
            continue
        res[start]=st[i]
        count[i]=count[i]-1
        permutation(st,count,res,start+1)
        count[i]=count[i]+1



if __name__ == '__main__':
    str='ABC'
    arr=list(str)
    dic={}
    data=[]
    count=[]
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for d in sorted(dic.keys()):
        data.append(d)
        count.append(dic[d])
    # print(dic)
    # print(data)
    # print(count)


    res=[0]*len(arr)
    permutation(data,count,res,0)
    print(len(temp))
