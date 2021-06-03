def sol(arr):
    n=len(arr)
    m=len(arr[0])
    print(n,m)
    #colum wise chek
    temp=0
    c=0
    ans=999999999
    for i in range (n):
        c=1
        for j in range (m):
            # print(i, j, '===> ', arr[i][j])
            if j+1<m:
                if arr[i][j]==arr[i][j+1]:
                    # print(arr[i][j], end="")
                    c+=1
                else:
                    c=0
                if c>=5:
                    print(arr[i][j])
                    ans=min(ans,arr[i][j])
                    c=0
    # print("COl se Ans :",ans)
    # row wise chek
    print("--------------------------")
    for i in range(m):
        c=1
        for j in range(n):
            if i + 1 < m and j + 1 < n:
                if arr[j][i] == arr[j+1][i]:
                    c += 1
                else:
                    c = 0
                if c >= 5:
                    # print(arr[j][i], end="")
                    ans = min(ans, arr[j][i])
                    c = 0
    return ans



def opti(arr,r,c):
    ans=[]
    for i in range (r):
        for j in range (c-2):
            if arr[i][j]==arr[i][j+1]==arr[i][j+2]:
                ans.append(arr[i][j])
    for i in range (r-2):
        for j in range (c):
            if arr[i][j] == arr[i+1][j] == arr[i+2][j]:
                ans.append(arr[i][j])




if __name__ == '__main__':
    arr=[
            [2 ,3 ,4, 5, 6, 2, 4],
            [2 ,3, 4 ,7 ,6 ,7 ,6],
            [2 ,3 ,5, 5 ,5 ,5 ,2],
            [2 ,3 ,1 ,1 ,2, 1 ,3],
            [1 ,1 ,1 ,1 ,9 ,0 ,3],
            [1 ,3, 1 ,1 ,5 ,1 ,2]
    ]
    print(sol(arr))