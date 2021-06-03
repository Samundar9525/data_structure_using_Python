def merge(arr):
    for i in range(len(arr)):
        if i + 1 < len(arr):
            if arr[i] == arr[i + 1]:
                arr.pop(i)
            elif (arr[i][0] == 0 and arr[i][1] == 0):
                pass
            elif(arr[i + 1][0] == 0 and arr[i + 1][1] == 0):
                pass

            else:
                print("hello")
                if arr[i][1] >= arr[i + 1][0]:
                    arr[i + 1][0] = min(arr[i + 1][0], arr[i][0])
                    arr[i + 1][1] = max(arr[i][1], arr[i + 1][1])
                    arr.pop(i)
            if i+1==len(arr):
                i=i-1
                if arr[i][1] >= arr[i + 1][0]:
                    arr[i + 1][0] = min(arr[i + 1][0], arr[i][0])
                    arr[i + 1][1] = max(arr[i][1], arr[i + 1][1])
                    arr.pop(i)

    return arr



arr=[[1,4],[0,2],[3,5]]
print(merge(arr))