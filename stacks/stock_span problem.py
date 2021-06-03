# maximum number of consecutive days just before the given day
# For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85},
# then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4 , 6}.

def sol(arr):
    n=len(arr)
    stk=[]
    res=[]
    for i in range (n):
        if len(stk)<1:
            res.append(-1)
        else:
            if arr[i]<stk[-1][0]:
                res.append(stk[-1][1])
            else:
                while(len(stk)!=0 and arr[i]>=stk[-1][0] ):
                    stk.pop()
                if (len(stk)<1):
                    res.append(-1)
                elif(arr[i]<stk[-1][0]):
                    res.append(stk[-1][1])
        stk.append([arr[i],i])
    print(res)
    for i in range(n):
        res[i]=i-res[i]
    return res

if __name__ == '__main__':
    arr=[100 ,80 ,60 ,70, 60 ,75 ,85]
    print(sol(arr))