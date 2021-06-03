import math
def solution(str):
    stk=[]
    for i in str:
        if i=='}':
            if len(stk)!=0:
                d=stk.pop()
                if d=='{':
                    continue  #koi dikkat nahi match ho gaya ab stack se relevant ud bhi jaye toh
                else:          #continue isliye lagaye taki ye '}' wala nahi jud paye and jo pop ho gaya wo ho gaya jane do
                    stk.append('}')
        stk.append(i)
    # print(stk)
    if len(stk)%2==0:
        m=0
        n=0
        for i in stk:
            if i=='{':
                m+=1
            else:
                n+=1
        m=m/2
        n=n/2
        m=math.ceil(m)
        n=math.ceil(n)
        # print(m,n)
        return m+n

    else:
        return -1

if __name__ == '__main__':
    str='}{{}}{{{'
    print(solution(str))