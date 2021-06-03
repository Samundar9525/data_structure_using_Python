def sol(arr,word,indx,i,j):
    count=0
    #basecases
    if i>=0 and j>=0 and i<n and j<n and word[indx]==arr[i][j]:
        temp=arr[i][j]
        arr[i][j]=0
        indx+=1
        if indx==n-1:
            count=1
        else:
            count+=sol(arr,word,indx,i+1,j)
            count+=sol(arr,word,indx,i-1,j)
            count+=sol(arr,word,indx,i,j+1)
            count+=sol(arr,word,indx,i,j-1)
        arr[i][j]=temp
    return count
            


inputt =[ "BBABBM",
              "CBMBBA",
              "IBABBG", 
              "GOZCBI",
              "ABCIBC",
              "MCIGAM"]
word='MAGIC'
n=len(inputt)
strr = [0] * len(inputt) 
for i in range(len(inputt)):  
    strr[i] = list(inputt[i])
#print(strr)
c=0
for i in range(n):
    for j  in range (n):
        c+=(sol(strr,word,0,i,j))

print(word ," present in array=> ",c,' times ')









