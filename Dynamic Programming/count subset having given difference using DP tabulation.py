def add(arr):
    temp=0
    for i in range(len(arr)):
        temp+=arr[i]
    return temp

#
# def check(tem):
#     if (tem % 2==0):
#         return True
#     else:
#         return False

def subset(arr,sum,n,t):
    for i in range(n+1):
        for j in range(sum+1):
            if j==0:
                t[i % 2][j]=True
            elif i==0:
                t[i % 2][j] = False
            elif(arr[i-1]>sum):
                #   --------------------------------reject kar do
                t[i % 2][j]=t[(i+1) % 2][j]

            else:
                #------------------------------------Accept karr do
                t[i % 2][j]=t[(i+1) % 2][j-arr[i-1]] + t[(i+1) % 2][j]
    return t[n % 2][sum]

if __name__ == '__main__':
    arr=[1,1,2,3]
    n=len(arr)
    diff=1
    su=add(arr)

    new_sum= (su+diff)//2
    t=[[False for i in range(new_sum + 1)] for j in range(2)]

    print("count: ",subset(arr,new_sum,n,t))


