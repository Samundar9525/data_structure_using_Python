def sol(arr,n):
    arr.append(0)
    hare=arr[1]
    tort=arr[1]
    while (True):
        hare=arr[arr[hare]]
        tort=arr[tort]
        if hare==tort:
            break
    tort=arr[1]

    while(hare!=tort):
        hare=arr[hare]
        tort=arr[hare]
    return hare







if __name__ == '__main__':
    n=3
    arr=[1, 3, 3]
    print(sol(arr,n))