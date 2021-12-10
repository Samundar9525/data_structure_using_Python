import copy
def sol(arr,row,col):
    top=0
    bottom=row-1
    left=0
    right=col-1
    # print(top,bottom,left,right)

    while(top<bottom and left<right):
        prev=arr[top+1][left]         # ye karna jaroori hai arr[top+1][0] nahi kar sakte kyunki ye sirf bhar wale ko hi traverse karega aandar ghusega hi nahi
        for i in range (left,right+1):
            curr=arr[top][i]
            arr[top][i]=prev
            prev=curr
        top+=1
        for i in range(top,bottom+1):
            curr=arr[i][right]
            arr[i][right]=prev
            prev=curr
        right-=1
        for i in range(right,left-1,-1):
            curr=arr[bottom][i]
            arr[bottom][i]=prev
            prev=curr
        bottom-=1

        for i in range (bottom,top-1,-1):
            curr=arr[i][left]
            arr[i][left]=prev
            prev=curr
        left+=1

def printMatrix(mat):
    for row in mat:
        print (row)


if __name__ == '__main__':
    # arr=[
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, 15,16]
    # ]

    arr=[[20 ,25 ,34 ,98, 39 ,87, 75, 38, 59 ,23, 52, 56, 30 ,33 ,8],
         [90, 44,28 ,69 ,73 ,97, 60, 71 ,47 ,45, 29 ,65, 91 ,82 ,33],
         [90, 32 ,49 ,85 ,95 ,58 ,3, 19 ,71 ,17 ,27 ,40 ,38, 67 ,33]]


    # arr = [[1,2],
    #        [5,6]]
    mat=copy.deepcopy(arr)
    temp=arr
    row=len(arr)
    col=len(arr[0])
    printMatrix(arr)
    for i in range (16):
        (sol(arr,row,col))
        print("@@@@@@@@@@@@\t" , i,"\t@@@@@@@@@@@@@@@@@@@@@")
        printMatrix(arr)
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # printMatrix(mat)
    #
