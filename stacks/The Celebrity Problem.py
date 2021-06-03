def sol(arr):
    n=len(arr)
    stk=[]
    for i in range (n):
        stk.append(i)
    while(len(stk)>1):
        num1=stk.pop(-1)
        num2=stk.pop(-1)

        if arr[num1][num2]==1:
            stk.append(num2)
        else:
            stk.append(num1)
    j=stk.pop()
    for i in range(n):
        if i==j and arr[i][j]==1:
            return -1
        elif arr[i][j]==0 and i!=j:
            return -1
        elif arr[j][i]==1 and i!=j:
            return -1
    return j
if __name__ == '__main__':
    arr=[[0,1,0],
         [0,0,0],
         [0,1,0]]
    print(sol(arr))