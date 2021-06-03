def sol(arr,n):
    t=[]
    for row in arr:
        for col in row:
            t.append(col)
    print(t)
    t.sort()
    print(t[n-1])

if __name__ == '__main__':
    Mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [24, 29, 37, 48],
           [32, 33, 39, 50]]
    n=7
    sol(Mat,n)