def sol(arr,n):
    stk=[]
    p=0
    for i in range(n):
        while(stk and stk[-1]<arr[i]):
            p=stk[-1]
            stk.pop()
        if arr[i]<p:
            print(arr[i],p)
            return False
        stk.append(arr[i])
    return True



if __name__ == '__main__':
    arr=[40,30,35,20,80,100]
    print(sol(arr,len(arr)))