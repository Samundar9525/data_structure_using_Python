def sol(arr):
    res=set(arr[0])
    for i in arr:
        t=set(i)
        res=res.intersection(t)
    print(res)



if __name__ == '__main__':
    arr=[
        [1, 2, 1, 4, 8],
        [3, 7, 8, 5, 1],
        [8, 7, 7, 3, 1],
        [8, 1, 2, 7, 9]
    ]
    sol(arr)