def transpose(arr,row,col):

    for i in range (row):
        for j in range (i):
            arr[i][j],arr[j][i]=arr[j][i],arr[i][j]



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
    transpose(arr,len(arr),len(arr[0]))
    print("")
    print("Original matrix : ", printMatrix(arr))