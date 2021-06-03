def reverse (arr):
    i=0; j=len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j][::-1],arr[i][::-1]
        i+=1
        j-=1

if __name__ == '__main__':
    arr=["my","name",'is','samundar']
    print(arr)
    reverse(arr)
    print(arr)

