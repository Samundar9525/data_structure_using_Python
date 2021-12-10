def NSL(arr):
    n=len(arr)
    stk=[]
    res=[]
    for i in range (n):
        if (len(stk)<1):
            res.append(-1)
        else:
            if arr[i]>stk[-1][0]:
                res.append(stk[-1][1])
            else:
                while(len(stk)!=0 and arr[i]<=stk[-1][0]):
                    stk.pop()
                if (len(stk)<1):
                    res.append(-1)
                elif(arr[i]>stk[-1][0]):
                    res.append(stk[-1][1])
        stk.append([arr[i],i])
    return res

def NSR(arr):
    n=len(arr)-1
    stk=[]
    res=[]
    bound=len(arr)
    for i in range (n,-1,-1):
        if len(stk)<1:
            res.append(bound)
        else:
            if arr[i]>stk[-1][0]:
                res.append(stk[-1][1])
            else:
                while(len(stk)!=0 and arr[i]<=stk[-1][0] ):
                    stk.pop()
                if len(stk) < 1:
                    res.append(bound)
                elif arr[i] > stk[-1][0]:
                    res.append(stk[-1][1])
        stk.append([arr[i],i])
    return res[::-1]

def sol(arr):
    left=NSL(arr)
    right=NSR(arr)
    print("NSL :",left)
    print("NSR : ",right)
    resultant=[]
    for i in range(len(arr)):
        resultant.append((right[i]-left[i])-1)
    for i in range (len(arr)):
        resultant[i]=resultant[i]*arr[i]
    return max(resultant)



if __name__ == '__main__':
    arr = [6, 2, 5, 4, 5, 1, 6]
    print(sol(arr))









####################################    ACCEPTED by leetcode  ########################################


# def one_function_anwer(arr):
#     n = len(arr)
#     stk = []
#     res = []
#     for i in range(n):
#         if (len(stk) < 1):
#             res.append(-1)
#         else:
#             if arr[i] > stk[-1][0]:
#                 res.append(stk[-1][1])
#             else:
#                 while (len(stk) != 0 and arr[i] <= stk[-1][0]):
#                     stk.pop()
#                 if (len(stk) < 1):
#                     res.append(-1)
#                 elif (arr[i] > stk[-1][0]):
#                     res.append(stk[-1][1])
#         stk.append([arr[i], i])
#     left = res
#     bound = n
#     n = n - 1
#     stk = []
#     res = []
#     bound = len(arr)
#     for i in range(n, -1, -1):
#         if len(stk) < 1:
#             res.append(bound)
#         else:
#             if arr[i] > stk[-1][0]:
#                 res.append(stk[-1][1])
#             else:
#                 while (len(stk) != 0 and arr[i] <= stk[-1][0]):
#                     stk.pop()
#                 if len(stk) < 1:
#                     res.append(bound)
#                 elif arr[i] > stk[-1][0]:
#                     res.append(stk[-1][1])
#         stk.append([arr[i], i])
#     right = res[::-1]
#
#     resultant = []
#     for i in range(len(arr)):
#         resultant.append((right[i] - left[i]) - 1)
#
#     for i in range(len(arr)):
#         resultant[i] = resultant[i] * arr[i]
#     return max(resultant)