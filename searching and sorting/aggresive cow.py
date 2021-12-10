def sol(stall,cow):
    stall.sort()
    low=stall[0]
    high=len(stall)-1
    ans=0

    while(low<=high):
        mid=(low+high)//2
        if possible(stall,mid,cow):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

def possible(stall,mid,cow):
    last=stall[0]
    count=1
    for i in range (len(stall)):
        if (stall[i]-last>=mid):
            count+=1
            last=stall[i]
        if count==cow:
            return True
    return False

if __name__ == '__main__':
    t=int(input())
    for _ in range (t):
        a=list(map(int,input().split()))
        stalllen=a[0]
        cow=a[1]
        stall=[]
        for i in range(stalllen):
            stall.append(int(input()))
        print(sol(stall,cow))
