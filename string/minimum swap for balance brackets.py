def sol(arr):
    n=len(arr)
    te=["|"]*n
    for i in range(n):
        if i%2==0:
            te[i]='['
        else:
            te[i]=']'
    print(arr)
    print(te)

    fl=0
    for i in range(n):
        if arr[i]!=te[i]:
            fl+=1
    return fl//2




if __name__ == '__main__':
    str='[[][[][]'
    str=list(str)
    print(sol(str))
