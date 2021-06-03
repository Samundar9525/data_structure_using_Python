import time
def subset(arr,n,sum,res):
    if (sum==0):
        sub.append(res)
        print(res)
        return
    if(n==0):
        return

    r=res+[]
    r.append(arr[n-1])

    reject = subset(arr, n - 1, sum, res)
    accept=subset(arr, n - 1, sum-arr[n-1], r)

def display(arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()
    print("--------------------")


if __name__ == '__main__':
    arr=[ x for x in range (1,20)]
    sum=20
    res=[]
    sub=[]
    start=time.time()
    subset(arr,len(arr),sum,res)
    time.sleep(0.1)
    end=time.time()
 
    print(" Execution Time :: ",end-start)
    print(len(sub))
