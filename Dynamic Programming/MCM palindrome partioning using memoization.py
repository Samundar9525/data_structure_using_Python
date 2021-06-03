def display(arr):
    for i in (arr):
        for j in i :
            print(j,end=" ")
        print("")

def palind(str,i,j):
    while(i<j):
        if str[i]!=str[j]:
            return False
        else:
            i=i+1
            j=j-1
    return True

def mcm(str,i,j,t):
    if i>=j:
        return 0

    if t[i][j]!=-1:
        return t[i][j]

    res=999999
    for k in range (i,j):
        if (palind(str, i, j)):
            return 0
        if t[i][k]!=-1:
            left=t[i][k]
        else:
            left=mcm(str, i, k, t)
            t[i][k]=left
        if t[k+1][j]!=-1:
            right= t[k+1][j]
        else:
            right=mcm(str,k+1,j,t)
            t[k+1][j]=right

        temp=left+right+1

        if temp<res:
            res=temp
            t[i][j]=res
            dir[i][j]=k
    return t[i][j]


if __name__ == '__main__':
    str="ababbbabbababaabbabffgdh"                      #output 9 ana chhaiye
    n=len(str)

    dir = [[0 for i in range(n+1)] for j in range(n+1)]
    t=[[-1 for i in range (n+1)] for j in range (n+1)]
    print("Mininmum number of cut : ",mcm(str,0,n-1,t))
    #print(t)
    #display(dir)
