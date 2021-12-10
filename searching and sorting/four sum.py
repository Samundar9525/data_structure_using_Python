def sol(ar,su):
    n=len(ar)
    ans=[]
    for i in range(n-3):
        for j in range(i+1,n-2):
            st=j+1
            en=n-1

            while(st<en):
                if ar[i]+ar[j]+ar[st]+ar[en]==su:
                    ans.append((ar[i],ar[j],ar[st],ar[en]))
                    st+=1
                    en-=1
                elif ar[i]+ar[j]+ar[st]+ar[en]<su:
                    st+=1
                else:
                    en-=1

    print(len(ans))
    if len(ans) == 0:
        return []
    ans=set(ans)
    ans=list(ans)
    ans.sort()
    return ans




if __name__ == '__main__':
    n=27
    sum=179
    arr=[88, 84, 3, 51, 54, 99 ,32, 60, 76 ,68, 39 ,12 ,26, 86, 94 ,39, 95 ,70 ,34 ,78 ,67 ,1 ,97 ,2 ,17 ,92 ,52]
    arr.sort()
    print(sol(arr,sum))
    print(len(sol(arr,sum)),'gottcha sala upar 83 aa raha tha isme 72 chutiya banta hai duplicate daal ke!!! ')