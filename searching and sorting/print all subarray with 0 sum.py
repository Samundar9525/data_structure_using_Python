def solution(arr,n):
    di={}
    cur=0
    c=0
    ans=[]
    for i in range(n):
        cur=cur+arr[i]
        if cur ==0:
            ans.append([0,i])
        if cur not in di:
            di[cur]=[i]
        else:
            te=di[cur]
            for j in range(len(te)):
                ans.append([te[j]+1,i])
            te.append(i)
            di[cur] = te
        print(ans)
    print(di)
    return ans

if __name__ == '__main__':
    arr=[6,-1,-3,4,-2,2,4,6,-12,-7]
    # arr=[0,0,5,5,0,0]
    # arr=[9, -10, -1, 5, 17, -18, 6, 19, -12, 5, 18, 14, 4, -19, 11, 8, -19, 18, -20, 14, 8, -14, 12, -12, 16, -11, 0, 3, -19, 16]
    n=len(arr)
    an=(solution(arr,n))
    for i in an:
        print("pattern found at :",i[0],"======>",i[1],end=" ")
        print(" i.e : [",end=" ")
        for k in range(i[0],i[1]+1):
            print(arr[k],end=" ")
        print("]")
    print("---------------------------------------------")
    print("\t\t\t\t\t\t\t    Total : ",len(an))