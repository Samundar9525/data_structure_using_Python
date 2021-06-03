def minjumps(arr,n):
    t=[0]*n

    for i in range(1,n):
        t[i]=999999
        for j in range(0,i):
            if j+arr[j]>=i:
                t[i]=min(t[i],t[j]+1)
                p[i]=j
                break
    if t[n-1]==999999:
        return "NOT POSSIBLE"
    return(t[n-1])

def tresspath(arr):
    dic={}
    for i in range (len(arr)-1,0,-1):
        if arr[i] not in dic:
            dic[arr[i]]=i
    print(dic.values())

if __name__ == '__main__':
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    # arr = [2, 1, 3, 2, 3, 4, 5, 1, 2, 8]
    # arr = [1,1,1,1,1,1]
    n=len(arr)
    p = [0] * n
    print(minjumps(arr,n))
