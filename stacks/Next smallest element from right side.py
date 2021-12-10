def sol(arr):
    n=len(arr)-1
    stk=[]
    res=[]
    for i in range(n,-1,-1):
        if len(stk)<=0:
            res.append(-1)
        else:
            if arr[i]>stk[-1]:
                res.append(stk[-1])
            else:
                while (len(stk)!=0 and arr[i]<=stk[-1]):
                    stk.pop()
                if len(stk)<=0:
                    res.append(-1)
                elif arr[i]>stk[-1]:
                    res.append(stk[-1])
        stk.append(arr[i])
    return res[::-1]

if __name__ == '__main__':
    arr = [4, 8, 5, 2, 25]
    print(sol(arr))