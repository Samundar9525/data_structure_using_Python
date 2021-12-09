def sol(arr):
    #negative no store karo
    neg=0
    largneg=-99999999999999
    flag=0
    for i in arr:
        if i <0:
            largneg=max(largneg,i)
            neg+=1
        if i==0:
            flag=1
    # print(largneg)
    if (neg)==0:
        return min(arr)

    if (neg)%2==0 and largneg!=-99999999999999:
        arr.remove(largneg)
    res=1
    for i in arr:
        if i ==0:
            continue
        res*=i
    return res

if __name__ == '__main__':
    arr=[ 2,5,-1,-2,-3,-4]
    # arr=[1,2,3,4,5,6,0]
    print(sol(arr))
