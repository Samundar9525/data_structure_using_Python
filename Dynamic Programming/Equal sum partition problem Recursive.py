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

def subset(arr,sum,n):
    if sum==0:
        return True
    if n==0:
        return False
    if (arr[n-1]>sum):
        reject=subset(arr,sum,n-1)
        return reject
    else:
        accept=(arr,sum-arr[n-1],n-1) or subset(arr,sum,n-1)
        return accept



if __name__ == '__main__':
    arr=[1,5,5,1]
    n=len(arr)
    #print(sum(arr,n))
    su=sum(arr,n)

    if (check(su)):
        if(subset(arr,su/2,n)):
            print("POssible ")
        else:
            print("Not possible ba ")
    else:
        print("NO Possible subset Exists sum  hi odd aa gaya toh")

