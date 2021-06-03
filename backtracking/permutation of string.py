def permutation(data, count, res, start):
    if(start==len(stri)):
        print(res)
        return

    for i in range(len(data)):
        if count[i] == 0:
            continue
        res[start] = data[i]
        count[i] = count[i] - 1
        permutation(data, count, res, start + 1)
        count[i] = count[i]+1


if __name__ == '__main__':
    strin="bccad"
    stri=list(strin)
    dict={}
    for i in stri:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=dict[i]
    data=[]
    count=[]
    for item,key in dict.items():
        data.append(item)
        count.append(key)
    res=[0]*len(stri)
    permutation(data,count,res,0)


