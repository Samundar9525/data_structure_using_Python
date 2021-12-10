def sol(arr):
    n=len(arr)
    stk=[]
    res=[]
    for i in range (n):
        if len(stk)<1:
            res.append(-1)
        else:
            if arr[i]>stk[-1]:
                res.append(stk[-1])
            else:
                while(len(stk)!=0 and arr[i]<=stk[-1]):
                    stk.pop()
                if len(stk)<1:
                    res.append(-1)
                elif arr[i]>stk[-1]:
                    res.append(stk[-1])
        stk.append(arr[i])
    return (res)

if __name__ == '__main__':
    arr = [4, 5, 2, 10, 8]
    print(sol(arr))