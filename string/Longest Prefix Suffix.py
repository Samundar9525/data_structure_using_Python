def sol(s):
    n = len(s)
    m=n-1
    ma=-9999
    c = 0
    pr = ''
    flag=0

    for i in range(n):
        su = ''
        pr += s[i]
        su += s[m-i:n]
        # su=su[::-1]
        # print(pr ,su)
        if pr==su and len(pr)!=n:
            flag=1
            ma=max(ma,len(pr))

    if flag==0:
        return 0
    else:
        return ma








if __name__ == '__main__':
    str='aaaa'
    print(sol(str))