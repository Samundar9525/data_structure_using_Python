def palind(str,i,j):
    while(i<j):
        if str[i]!=str[j]:
            return False
        else:
            i=i+1
            j=j-1
    return True

def mcm(str,i,j):
    if i>=j:
        return 0

    if (palind(str,i,j)):
        return 0

    res=999999
    for k in range (i,j):
        temp=mcm(str,i,k)+mcm(str,k+1,j)+1

        if temp<res:
            res=temp
    return res


if __name__ == '__main__':
    str="ababbbabbababa"                #output     3 ana chhaiye
    #print(palind(str,0,len(str)-1))

    print(mcm(str,0,len(str)-1))