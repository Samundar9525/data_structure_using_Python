def sol(s):
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
    return (stk[-1])


if __name__ == '__main__':
    s="*-A/BC-/AKL"
    print(sol(s))