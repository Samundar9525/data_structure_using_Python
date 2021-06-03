def dupchecker(arr):
    t=arr[0]
    h=arr[0]
    while True:
        t=arr[t]
        h=arr[arr[h]]
        print("tortoise : ",t)
        print("hare : ",h)
        if t==h:
            break
    print("-------------------------------------------------------")
    t=arr[0]
    while(t!=h):
        print("tortoise====> : ", t)
        print("hare=========> : ", h)
        t=arr[t]
        h=arr[arr[h]]
    print("tortoise====> : ", t)
    print("hare=========> : ", h)
    return (h)


if __name__ == '__main__':
    arr=[2,6,4,1,3,1,5]
    # arr=[2,1,3,4,2]
    print(dupchecker(arr))


