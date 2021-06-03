def count(arr,dict):
    for i in arr:
        if i not in dict:
            dict[i]=1
        else:
            dict[i]=dict[i]+1


if __name__ == '__main__':
    arr=[2,2,3,4,2,4,4,3,3,7,5,5,5,5,5,8,8,8,8]
    dict={}
    count(arr,dict)
    #print(dict)
    arr=list(dict.keys())
    brr=list(dict.values())

    pikt={}

    for i in range (len(arr)):
        if brr[i] not in pikt:
            pikt[brr[i]]=[arr[i]]
        else:
            k=[]
            k=pikt[brr[i]]
            k.append(arr[i])
            pikt[brr[i]]=k
    #print(pikt)
    kw=[]
    for key,val in sorted(pikt.items(),reverse=True):
        for j in val:
            kw.append (key*str(j).split())

    for i in kw:
        for j in i :
            print(j,end=" ")