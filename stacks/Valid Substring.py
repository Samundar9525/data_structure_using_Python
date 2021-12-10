def sol(s):
    stk=[]
    stk.append(-1)
    result=0
    for i in range (len(s)):
        if s[i]=="(":
            stk.append(i)
        else:
            if len(stk)!=0:
                stk.pop()
    # print(stk)
            if len(stk) != 0:
                result = max(result,i - stk[-1])
            else:
                stk.append(i)

    return result


if __name__ == '__main__':
    s="))()(()"
    s=")(())((()))"
    s="()))(())("
    print(sol(s))


# def sol2(arr):
#     l = 0
#     r = 0
#     ma = -999999999
#     for i in s:
#         if i == "(":
#             l += 1
#         else:
#             r += 1
#
#         if l == r:
#             ma = max(ma, l * 2)
#         elif l < r:
#             l = 0
#             r = 0
#     l = 0
#     r = 0
#     for i in range(len(s) - 1, -1, -1):
#         if s[i] == "(":
#             l += 1
#         else:
#             r += 1
#
#         if l == r:
#             ma = max(ma, r * 2)
#         elif l > r:
#             l = 0
#             r = 0
#     if ma < 0:
#         return 0
#     return ma
