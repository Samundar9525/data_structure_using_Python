def transpose(arr,row):

    for i in range (row):
        for j in range (i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]

def reversematrix_rowwise(arr):
    row=len(arr)
    for i in range (row):
        left=0
        right=row-1
        while(left<right):
            arr[i][left],arr[i][right]=arr[i][right],arr[i][left]
            left+=1
            right-=1
    return arr


def reversematrix_colwise(arr):
    col=len(arr[0])
    for i in range (col):
        top=0
        bot=col-1
        while(top<bot):
            arr[top][i],arr[bot][i]=arr[bot][i],arr[top][i]
            top+=1
            bot-=1
    return arr
def printMatrix(mat):
    print("############################################")
    for row in mat:
        print (row)
    print("############################################")

if __name__ == '__main__':
    arr=[
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15,16]
    ]
    print("Original matrix : ",printMatrix(arr))
    transpose(arr,len(arr))
    print("Transpose : ", printMatrix(arr))
    # arr=reversematrix_rowwise(arr)
    # print("90 degree in clockwise: ", printMatrix(arr))
    brr = reversematrix_colwise(arr)
    print("90 degree in Anti clockwise: ", printMatrix(brr))