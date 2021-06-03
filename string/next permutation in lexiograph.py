def reverse(arr,i,j):
    while(i<=j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr


arr=[62 ,92, 96, 43 ,28, 37, 92, 5 ,3 ,54, 93 ,83 ,22]
#arr=[1,2,3,6,5,4]
#arr=[5,1,1]
n=len(arr)

i=n-1
while(i>-1):
    if arr[i]>arr[i-1]:
        break
    i-=1
i=i-1
print(arr[i])
if i ==-1:
    reverse(arr,0,n-1)
    print(arr)
else:
    indx1=i

#print(arr[indx1])
mi=arr[indx1]
ma=arr[indx1+1]
indx2=0
for k in range (indx1,n):
    if arr[k]>mi and arr[k]<=ma:
        ma=max(ma,arr[k])
        indx2=k


arr[indx1],arr[indx2]=arr[indx2],arr[indx1]
#print(arr)
reverse(arr,indx1+1,n-1)
print(arr)
