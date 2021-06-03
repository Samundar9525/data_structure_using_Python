def display (arr):
    for i in arr:
        for j in i:
            print(j,end=" ")
        print()

def sum(arr,n):
    sum=0
    for i in range(n):
        sum+=arr[i]
    return sum

def check(sum):
    if sum%2==0:
        return True
    else:
        return False

def subset(arr,summ,n,t):
    for i in range(n+1):
        for j in range (summ+1):
            if j==0:
                t[i % 2][j]=True
            elif i==0:
                t[i % 2][j]=False
            elif(arr[i-1]>j):
                #  reject karwa do
                t[i % 2][j]=t[(i + 1) % 2][j]
            else:
                # yahan par accept karwa do
                t[i % 2][j]=t[(i+1) % 2][j-arr[i-1]] or t[(i + 1) % 2][j]
    return t[n % 2][summ]


if __name__ == '__main__':
    arr=[100,200,200]
    n=len(arr)
    #print(sum(arr,n))
    su=sum(arr,n)

    if (check(su)):
        s=su//2     # int mme conversion jarooriu hai sum ko half kiya ja raha hai
        t = [[False for i in range(s+ 1)] for j in range(2)]
        if(subset(arr,s,n,t)):
            print("POssible ")
        else:
            print("Not possible ba ")
    else:
        print("NO Possible subset Exists sum  hi odd aa gaya toh")

