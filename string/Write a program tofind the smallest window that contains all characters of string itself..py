def sol(str,di):
    n=len(str)
    su=len(di)
    st=0
    en=0
    pi={}
    ans=[]
    m=0
    for i in range(n):
        if str[i] not in pi:
            pi[str[i]]=1
            en+=1
        else:
            pi[str[i]]+=1
            en+=1
        if pi[str[i]]==di[str[i]]:
            m+=1
        if m==su:
            while(st<en and en<=n):
                ans.append(str[st:en])
                if pi[str[st]]>=1:
                    pi[str[st]]-=1
                if pi[str[st]] < di[str[st]]:
                    m -= 1
                    st += 1
                    break
                st += 1
    return((min(ans,key=len)))
    # return (len(min(ans, key=len)))
0
if __name__ == '__main__':
    str='aabcbcdbca'
    di={}
    for i in str:
        if i not in di:
            di[i]=1
    print(sol(str,di))