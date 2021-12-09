def sol(st):
    n=len(st)
    di=[]
    for i in st:
        if i not in di:
            di.append(i)
    # print(di)
    di.sort()
    print(di)
    mi=""
    ma=""
    for i in range(n):
        if di:
            k=di.pop(0)
        # print(st[i],k)
            if st[i]>k:
                mi=di[0]
                ma=st[i]
                break

    print(mi,ma)
    res=""
    for i in range(n):
        if st[i]==ma:
            res+=mi
        elif st[i]==mi:
            res+=ma
        else:
            res+=st[i]
    return res







if __name__ == '__main__':
    st="abcdefghijklabcdefghijklpop"     # chhaiye abbkc
    print(sol(st))