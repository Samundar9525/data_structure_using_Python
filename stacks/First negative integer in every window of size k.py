#  https://practice.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1#








############        NOt DONE PLEASE FINISH ME   ##############################











def NSL(arr,k):
    n=len(arr)-1
    stk=[]
    mi=9999999999
    # for i in range(k):
    #     if arr[i]<0:
    #         stk.append(arr[i])
    #         break
    res=[]
    for i in range (n,k,-1):
        if len(stk)<1:
            res.append(0)
        else:
            if arr[i]>stk[-1]:
                res.append(stk[-1])
            else:
                c=0
                while(len(stk)!=0 and arr[i]<stk[-1] and c<k-1):
                    c+=1
                    stk.pop()
                if len(stk) < 1:
                    res.append(0)
                elif arr[i] > stk[-1]:
                    res.append(stk[-1])

        stk.append(arr[i])
    print(res)






if __name__ == '__main__':
    arr=[12, -1, -7, 8, -15, 30, 16, 28]
    NSL(arr,3)
