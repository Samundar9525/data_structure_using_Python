def sol(arr):
    n=len(arr)
    re1=['0']*n
    re2=['0']*n

    for i in range (n):
        if i%2==0:
            re1[i]='1'
            re2[i]='0'
        else:
            re1[i]='0'
            re2[i] = '1'
    t1=0
    t2=0
    for i in range(n):
        if arr[i]!=re1[i]:
            t1+=1
        if arr[i]!=re2[i]:
            t2+=1
    print(t1,t2)
    return min(t1,t2)


if __name__ == '__main__':
    st='0001010111'
    str=list(st)
    print(sol(str))
