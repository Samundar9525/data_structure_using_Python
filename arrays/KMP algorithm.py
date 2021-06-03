def computeLPSArray(pat, M, lps):
    len = 0

    lps[0]=0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
            #print(lps,len)
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
                #print(lps,len)

def kmpalgo(txt,pat,n,m):
    i=0
    j=0
    k=0
    while i<n:          # lengh of text
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            k=k+1
            print("patrern found in  : ",i-j,"---",i-j+m)
            j=lps[j-1]              #  ye line isliye taki agar multiple pattern huae toh usko find kaar sake
        elif (i<n and pat[j]!=txt[i]):
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return k



if __name__ == '__main__':

    txt="ZABCDBABCQ"
    pat="ABC"
    n=len(txt)
    m=len(pat)
    lps = [0] * m

    computeLPSArray(pat, m, lps)
    print("total patter found : ",kmpalgo(txt,pat,n,m))
