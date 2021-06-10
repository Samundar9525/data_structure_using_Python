def sol(s):
    n = len(s)
    stk = []
    ptk = []
    for i in range(n):
        if s[i].isalpha():
            stk.append(s[i])
        else:
            if len(stk) >= 2:
                op1=stk.pop(-1)
                op2=stk.pop(-1)
                re = "(" + op2 + s[i] + op1 + ")"
                stk.append(re)
    return (stk[-1])


if __name__ == '__main__':
    s="*-A/BC-/AKL"
    s="ab*c+"
    print(sol(s))