def removedup(arr):
    j=0
    for i in range (len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr[j]=arr[i]
            j+=1
    arr[j]=arr[len(arr)-1]
    j+=1
    return j


def rem(arr):
    temp=[]
    for i in range (len(arr)-1):
        if arr[i]!=arr[i+1]:
            temp.append(arr[i])
    temp.append(arr[(len(arr)-1)])
    return  temp


if __name__ == '__main__':
    arr=[1,2,3,3,4,7,7,11,11,11,11,23,23,23,45,45,45]
    # j=removedup(arr)
    #
    # for i in range (0,j):
    #     print(arr[i],end=" ")
    # print("\n arr : ",arr)
    #

    temp=rem(arr)
    print(temp)