def sol(arr):
    t=[]
    for row in arr:
        for j in row:
            t.append(j)

    t.sort()
    print(t)
    n=len(arr)
    j=0
    arr=[]
    for i in range(n):
        arr.append((t[j:n+j]))
        j+=n
    print(arr)



if __name__ == '__main__':
    Mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    sol(Mat)