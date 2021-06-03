def display(arr):
    for i in (arr):
        for j in i :
            print(j,end=" ")
        print("")

def mcm(arr,i,j,t):
    if i>=j :
        return 0
    if t[i][j]!=-1:
        return t[i][j]
    res=999999
    for k in range(i,j):
        temp=mcm(arr,i,k,t)+mcm(arr,k+1,j,t) +(arr[i-1]*arr[k]*arr[j])

        if temp<res:
            res=temp
            t[i][j]=res
    return t[i][j]

if __name__ == '__main__':
    arr=[40,20,30,10,30]
    #arr = [10, 20, 30, 40, 30]
    #arr = [10, 20, 30]
    t=[[-1 for i in range(len(arr)+1)] for j in range (len(arr)+1)]
    print("minimum cost :  ",mcm(arr,1,len(arr)-1,t))
    #display(t)