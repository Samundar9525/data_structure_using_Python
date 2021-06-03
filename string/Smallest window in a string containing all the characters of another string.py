def sol(str,di):
    n=len(str)
    su=sum(di.values())
    st=0
    en=0
    pi=di
    ans=[]
    m=0
    print(pi,di)
    for i in range(n):
        if str[i] in pi:
            pi[str[i]]-=1
            if pi[str[i]] < 0:
                pi[str[i]] = (-1)
            en+=1
            if pi[str[i]]==0:
                m+=1













if __name__ == '__main__':
    str= "timetopractice"
    pat="toc"
    di={}
    for i in pat:
        if i not in di:
            di[i]=1
        else:
            di[i]+=1
    print(sol(str,di))