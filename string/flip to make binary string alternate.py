def sol(arr):
    n=len(arr)
    res=['0']*n
    for i in range(1,n,2):
        res[i]='1'
    print(arr)
    print(res)
    flip=0
    for i in range (n):
        if arr[i]!=res[i]:
            flip+=1
    return flip







if __name__ == '__main__':
    str='001'
    str=list(str)
    print(sol(str))