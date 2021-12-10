def sol(arr):
    ro=len(arr)
    col=len(arr[0])
    for row in arr:
        row.append(sum(row))
    ma=-99999999
    c=0
    for i in range (ro):
        if (arr[i][col])>ma:
            ma=arr[i][col]
            c=i
    print(c)


if __name__ == '__main__':
    arr=[
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1]
    ]

    # arr=[[0,0],[0,0]]
    sol(arr)
