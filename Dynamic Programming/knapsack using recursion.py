def knapsack(wt,val,w,n,res):
    if n==0 or w==0:
        return res
    if (wt[n-1]>w):
        return knapsack(wt,val,w,n-1,res)
    else:
        return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1,res),knapsack(wt,val,w,n-1,res))

if __name__ == '__main__':
    val=[10,15,40]
    wt=[1,2,3]
    w=6

    print(knapsack(wt,val,w,len(val),0))