def naive_rotate(arr,k):
    n=len(arr)
    temp=[]
    for i in range (n-k,n):
        temp.append(arr[i])
    print(temp)
    temp2=[]
    for j in range (n-k):
        temp2.append(arr[j])        #time complexity O(n)
    print(temp2)                   #space complexity O(n)
    return temp+temp2







if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    k=3
    print(naive_rotate(arr,k))
