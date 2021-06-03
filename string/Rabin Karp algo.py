def solution(str,pat):
    n=len(str)
    m=len(pat)
    god=101       # agar calculation ko reduce karna hai toh 101 ka chanda dena hoga
    d=256
    hash=1
    p=0
    t=0

    # creating hash value
    for i in range (m-1):
        # hash=(hash * d)
        hash=(hash * d) % god

    # finding hash value of the pattern

    for i in range (m):
        p=(p*d + ord(pat[i])) % god
        t=(t*d + ord(str[i])) % god
    # this will create the base of the sliding window and this is necessary since
    #we have to slide only one in next itereation and check that the string is matching or not

    #print(p,t)


    for i in range(n-m+1):
        if p==t:
            # then we have to check each alphabet one by one
            k=0
            for k in range(m):
                if str[i+k]!=pat[k]:
                    break
            #since iteration start from 0 so  k==m-1
            if k==m-1:
                print("FOUND at :  ",i)
        if i<n-m:
            t=(d*(t-ord(str[i])*hash)+ord(str[i+m])) %god

            if t < 0:
                t =0
            # agara negative chal jayega toh calculation me dikkat ho jayega

if __name__ == '__main__':
    str="AABAACAADAABAABA"
    pat='AABA'
    (solution(str,pat))