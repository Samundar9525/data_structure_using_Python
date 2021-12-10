def prefix_to_infix(s):
    n = len(s)
    stk = []
    ptk = []
    for i in range(n - 1, -1, -1):
        if s[i].isalpha():
            stk.append(s[i])
        else:
            if len(stk) >= 2:
                re = "(" + stk.pop(-1) + s[i] + stk.pop(-1) + ")"
                stk.append(re)
    return(stk[-1])

def infix_to_postfix(s):
    stk = []
    res = ""
    for i in s:
        if i.isalpha():
            res += (i)
        else:
            if len(stk) > 0:
                if i == "^":
                    stk.append(i)
                elif i == "*":
                    while (len(stk) != 0 and stk[-1] == "^" or stk[-1] == "*"):
                        res += (stk.pop())
                    stk.append(i)
                elif i == "/":
                    while (len(stk) != 0 and (stk[-1] == "^" or stk[-1] == "*" or stk[-1] == "/")):
                        res += (stk.pop())
                    stk.append(i)
                elif i == "+":
                    while (len(stk) != 0 and (
                            stk[-1] == "*" or stk[-1] == "/" or stk[-1] == "^" or stk[-1] == "+" or stk[-1] == "-")):
                        res += (stk.pop())
                    stk.append(i)
                elif i == "-":
                    while (len(stk) != 0 and (
                            stk[-1] == "*" or stk[-1] == "/" or stk[-1] == "^" or stk[-1] == "+" or stk[-1] == "-")):
                        res += (stk.pop())
                    stk.append(i)
                elif (i == "("):
                    stk.append(i)
                elif i == ")":
                    while (len(stk) != 0 and stk[-1] != "("):
                        res += (stk.pop())
                    stk.pop()
            else:
                stk.append(i)
    while (len(stk) != 0):
        res += (stk.pop())
    return(res)

def sol(s):
    r=prefix_to_infix(s)
    ans=infix_to_postfix(r)
    return(ans)


def optimised(s):
    n=len(s)
    stk=[]
    for i in range (n-1,-1,-1):
        if s[i].isalpha():
            stk.append(s[i])
        else:
            if len(stk)>=2:
                res=stk.pop(-1)+stk.pop(-1)+s[i]
                stk.append(res)
            else:
                stk.append(s[i])
    return stk[-1]

if __name__ == '__main__':
    s="*-A/BC-/AKL"
    print(sol(s))
    print(optimised(s))