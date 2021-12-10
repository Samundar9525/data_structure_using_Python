def sol(arr, n):
    pro = 1
    flag = 0
    i = 0
    memory = 0
    for i in range(n):
        if arr[i] == 0:
            pro *= 1
        else:
            pro *= arr[i]
    ans = []
    for i in range(n):
        if arr[i] == 0:
            flag = 1
            memory = i
            break
        else:
            ans.append(pro // arr[i])

    if flag == 1:
        for k in range(i + 1, n):
            if arr[k] == 0:
                tem1 = [0] * n
                return tem1

        temp = [0] * n
        temp[memory] = pro
        print(pro)
        return temp
    else:
        return ans




if __name__ == '__main__':
    # arr=[10, 3, 5, 6, 2]
    # arr=[12,0,3]
    arr=[1,0]
    # arr=[0, 8, 6, 2, 4, 7, 9, 3, 9, 2, 8, 3, 0, 1, 7, 8, 9, 1, 5, 4, 9, 2, 5, 7, 4, 9, 9, 4]
    n=len(arr)

    print(sol(arr,n))