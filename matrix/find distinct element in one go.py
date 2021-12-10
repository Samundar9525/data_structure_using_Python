def sol(arr):
    tem=[]
    for row in arr:
        tem.append(set(row))
    res=tem[0]
    print(res)
    tem.pop(0)
    for row in tem:
        res=row.intersection(res)
    print(len(res))


if __name__ == '__main__':
    arr=[
        [2, 1, 4, 3],
        [1, 2, 3, 2],
        [3, 6, 2, 3],
        [5, 2, 5, 3]
    ]
    sol(arr)
