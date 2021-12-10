def sol(arr,n):
    old=[]
    for i in range (n):
        old.append((arr[i],i))
    #print(old)
    old.sort()
    #print(old)
    swap=0
    j=0
    while(j<n):
        if (old[j][1])!=j:
            tem=old[j][1]
            old[j],old[tem]=old[tem],old[j]
            #print(old)
            #print(old[j][0],' swaps with ',old[tem][0])
            swap+=1
            j=j-1
        j=j+1
    return swap


if __name__ == '__main__':
    arr=[13, 1 ,5 ,3, 6 ,11, 10]
    n=len(arr)
    print(sol(arr,n))
