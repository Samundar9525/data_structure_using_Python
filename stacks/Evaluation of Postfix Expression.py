def operation(a, b, sym):
    if sym == "+":
        return a + b
    elif sym == "-":
        return a - b
    elif sym == "*":
        return a * b
    elif sym == "/":
        return a // b

def sol(S):
    arr = list(S)
    stk = []
    for i in arr:
        if len(stk) > 1 and i == "+" or i == "-" or i == "*" or i == "/":
            num1 = stk.pop()
            num2 = stk.pop()
            res = operation(num2, num1, i)
            stk.append(res)
        else:
            stk.append(int(i))
    return stk[-1]

if __name__ == '__main__':
    S = "231*+9-"
    print(sol(S))