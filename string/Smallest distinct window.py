def sol(str, di):
    n = len(str)
    su = sum(di.values())
    st = 0
    en = 0
    pi = di
    ans = []
    m = 0
    print(pi, di)
    for i in range(n):
        if str[i] in pi:
            pi[str[i]] -= 1
            if pi[str[i]] < 0:
                pi[str[i]] = (-1)

            if pi[str[i]] == di[str[i]]:
                m+=1
        en += 1
        print(m,su)
        if su==m:
            while(st<en and en<=n):
                if str[st] in pi:
                    pi[str[st]]+=1
                    if pi[str[st]]>=1:
                        m-=1
                        break
                    if pi[str[st]]<=0:

                        print(pi)
                st+=1
            if su<=len(str[st:en]):
                ans.append(str[st:en])
    print(ans)

if __name__ == '__main__':
    str = "zoomlazapzo"
    pat = "oza"
    di = {}
    for i in pat:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1
    print(sol(str, di))