def merge(arr,brr):
    n=len(arr)
    m=len(brr)
    res=[0]*(m+n)
    i=0
    j=0
    k=0

    while i<n and j<m:
        if arr[i]<brr[j]:
            res[k]=arr[i]
            k+=1
            i+=1
        # elif arr[i]==brr[j]:
        #     res[k]=arr[i]
        #     k+=1
        #     i+=1
        #     j+=1
        else:
            res[k]=brr[j]
            k+=1
            j+=1

    while(i<n):
        res[k]=arr[i]
        i+=1
        k+=1
    while(j<m):
        res[k]=brr[j]
        j+=1
        k+=1
    return res

if __name__ == '__main__':
    arr=[1,5,9,11,13,17,23]
    brr=[2,4,6,8,12,16,20,21]
    crr=[10,15,25]
    drr=[3,7,14,18,19,22,24]
    mas=[]
    mas.append(arr);mas.append(brr);mas.append(crr);mas.append(drr)
    #print(mas)
    t=len(mas)
    #print(merge(arr,brr))
    u=0
    x1=0
    result=[0]
    while(u<t):
        result=merge(result,mas[x1])
        x1+=1
        u+=1
    result.pop(0)
    print(result)