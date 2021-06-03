import time
def subset(arr,sum,res,n,sub):
    #display(t)
    if sum==0:
        sub.append(res)
        print(res)
        return res
    if n<0 or sum<0:
        return []

    if t[n][sum]!=-1:
        return t[n][sum]+[]
    r=res+[]
    r.append(arr[n-1])
    if (arr[n-1]>sum):
        t[n-1][sum]=subset(arr,sum,res,n-1,sub)
        return []+t[n-1][sum]
    else:
        t[n-1][sum] = subset(arr, sum - arr[n - 1], r, n - 1, sub) + subset(arr,sum,res,n-1,sub)
        return []+t[n-1][sum]




def display(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print("--------------------")


if __name__ == '__main__':
    arr=[x for x in range (1,20)]
    k=25
    res=[]
    sub=[]
    n=len(arr)
    start=time.time()
    t=[[-1 for i in range (k+1)]for j in range (n+1)]
    subset(arr,k,res,n,sub)
    time.sleep(0.1)
    end=time.time()

    print(" Execution Time :: ",end-start)
    #display(sub)

    print(len(sub))