def sol(arr,row,col):
    top=0
    bot=row-1
    left=0
    right=col-1
    ans=[]
    while(top<=bot and left<=right):
        for i in range (left, right+1):
            # print(arr[top][i])
            ans.append(arr[top][i])
        top+=1
        for i in range (top,bot+1):
            # print(arr[i][right])
            ans.append(arr[i][right])
        right-=1

        if top<=bot:
            for i in range (right,left-1,-1):
                # print(arr[bot][i])
                ans.append(arr[bot][i])
            bot-=1
        if left<=right:
            for i in range(bot,top-1,-1):
                # print(arr[i][left])
                ans.append(arr[i][left])
            left+=1
    return  ans


if __name__ == '__main__':
    arr=[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15,16]
    ]
    row=len(arr)
    col=len(arr[0])
    print(sol(arr,row,col))
