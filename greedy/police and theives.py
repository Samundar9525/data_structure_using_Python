def find(arr,k):
    p=[]
    t=[]
    for i in range(len(arr)):
        if arr[i]=="P":
            p.append(i)
        else:
            t.append(i)
    # print(p,t)
    # Let l and r be the variabe whose work is to run a loop till we traversed all the array of the police and theif
    l=0
    r=0
    res=0
    while (l<len(p) and r<len(t)):
        if abs(p[l]-t[r])<=k:
            res+=1
            l+=1
            r+=1
        elif p[l]<t[r]:
            l+=1
        else:
            r+=1
    return res



if __name__ == '__main__':
    print("hello")
    arr=['T', 'T', 'P', 'T', 'P', 'P']
    print(arr)
    print("police itna chor ko pakda : ",find(arr,2 ))
