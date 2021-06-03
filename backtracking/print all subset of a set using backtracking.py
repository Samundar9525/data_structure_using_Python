def subset(arr,res,n,sub):
    if len(res)>0:
        display(res)
    sub.append(res+[])
    for i in range(n,len(arr)):
        res.append(arr[i])
        subset(arr,res,i+1,sub)
        res.pop()
    return

def display(arr):
    for i in arr:
        print(i,end="")
    print()


if __name__ == '__main__':
    #arr=[1,2,3,3,3,3]
    #arr=['a','b','c']
    #arr=input()
    #arr=set(arr)
    arr='abc'
    arr=list(arr)
    arr.sort()
    n=len(arr)
    res=[]
    sub=[]
    subset(arr,res,0,sub)
    sub.sort()
    print(sub)
