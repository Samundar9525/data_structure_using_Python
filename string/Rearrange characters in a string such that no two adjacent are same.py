def sol(str,di,c):
    t=['0']*sum(di.values())
    curr=''
    ans=''
    st=0
    en=len(t)-1
    print(di)

















if __name__ == '__main__':
    str='geeksforgeeks'
    di={}
    c=0
    for i in str:
        if i not in di:
            di[i]=1
        else:
            di[i]+=1
            c+=1
    # print(di)
    print(sol(str,di ,c))


