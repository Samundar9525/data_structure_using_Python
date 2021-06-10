def sol(s):
    stk=[]
    res=[]
    for i in s:
        if i.isalpha():
            res.append(i)
        else:
            if len(stk)>1:
                if i =="(":
                    stk.append("(")
                elif(i=="*" or i=="/"):
                    while len(stk)!=0 and  stk[-1]=="^" :
                        res.append(stk.pop())
                    if i=="/" and stk[-1]=="*":
                        res.append(stk.pop())
                    stk.append(i)
                elif(i=="+" or i=="-"):
                    while len(stk) != 0 and (stk[-1] == "^" or stk[-1] == "*" ):
                        res.append(stk.pop())
                    if i=="-" and stk[-1]=="+":
                        res.append(stk.pop())
                    stk.append(i)
                elif (i == "^" or i == "*" or i=="/"):
                    while len(stk) != 0 and (stk[-1] == "+" or stk[-1]=="-"):
                        res.append(stk.pop())
                    stk.append(i)
                elif (i==")"):
                    while(stk[-1]!="("):
                        res.append(stk.pop())
                    stk.pop()
            else:
                stk.append(i)
    while(len(stk)!=0):
        res.append(stk.pop())
    result=""
    for i in res:
        result+=i
    print(result)

def sol2(s):
    stk=[]
    res=""
    for i in s:
        if i.isalpha():
            res+=(i)
        else:
            if len(stk)>0:
                if i=="^":
                    stk.append(i)
                elif i=="*":
                    while ( len(stk)!=0 and stk[-1] == "^" or stk[-1] == "*"):
                        res+=(stk.pop())
                    stk.append(i)
                elif i=="/":
                    while (len(stk)!=0 and (stk[-1] == "^" or stk[-1]=="*" or stk[-1] == "/")):
                        res+=(stk.pop())
                    stk.append(i)
                elif i=="+":
                        while(len(stk)!=0 and( stk[-1] =="*" or stk[-1]=="/" or stk[-1]=="^" or stk[-1] == "+"  or stk[-1] == "-" )):
                            res+=(stk.pop())
                        stk.append(i)
                elif i=="-":
                    while (len(stk)!=0 and(stk[-1] == "*" or stk[-1] == "/" or stk[-1] == "^" or stk[-1] == "+" or stk[-1] == "-")):
                        res+=(stk.pop())
                    stk.append(i)
                elif(i=="("):
                    stk.append(i)
                elif i==")":
                    while(len(stk)!=0 and stk[-1]!="("):
                        res+=(stk.pop())
                    stk.pop()
            else:
                stk.append(i)
    while(len(stk)!=0):
        res+=(stk.pop())
    print(res)

if __name__ == '__main__':
    s="a+b*(c^d-e)^(f+g*h)-i"                  # ab+c+d/
    s="(a*b)-(c*d)+(e/f)"           #ab*cd*-ef/+
    sol2(s)






