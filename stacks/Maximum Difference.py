def NSL(arr):
    n=len(arr)
    stk=[]
    res=[]
    for i in range(n):
        if len(stk)<1:
            res.append(0)
        else:
            if arr[i]>stk[-1]:
                res.append(stk[-1])
            else:
                while(len(stk)!=0 and arr[i]<=stk[-1]):
                    stk.pop()
                if len(stk)<1:
                    res.append(0)
                elif(arr[i]>stk[-1]):
                    res.append(stk[-1])
        stk.append(arr[i])
    return(res)

def NSR(arr):
    n=len(arr)-1
    stk=[]
    res=[]
    for i in range(n,-1,-1):
        if len(stk)<1:
            res.append(0)
        else:
            if stk[-1] < arr[i]:
                res.append(stk[-1])
            elif stk[-1]>=arr[i]:
                while(len(stk)!=0 and stk[-1]>=arr[i]):
                    stk.pop()
                if len(stk)<1:
                    res.append(0)
                elif stk[-1]<arr[i]:
                    res.append(stk[-1])
        stk.append(arr[i])

    return(res[::-1])


def sol(arr):
    R=NSL(arr)
    l=NSR(arr)
    ma=-999999999999
    for i in range(len(l)):
        ma=max(abs(l[i]-R[i]),ma)
    return ma



if __name__ == '__main__':
    arr=[2, 4, 8, 7, 7, 9, 3]
    print(sol(arr))