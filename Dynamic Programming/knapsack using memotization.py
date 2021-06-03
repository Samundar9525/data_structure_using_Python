def knapsack(wt,val,w,n):

    if n==0 or w==0:
        t[n][w]=0
    if t[n][w]!=-1:
        return t[n][w]
    display(t)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    if wt[n-1]>w:
        t[n][w]=knapsack(wt,val,w,n-1)
        display(t)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    else:
        t[n][w] =max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1),knapsack(wt,val,w,n-1))
        display(t)
        print("-----------------------")
    return t[n][w]




def display(arr):
    for i in (arr):
        for j in i :
            print(j,end=" ")
        print("")


if __name__ == '__main__':
    wt=[1,2,3]
    val=[25,25,40]
    w=3
    n=len(val)
    t=[[-1 for i in range (w+1)]for j in range (n+1)]
    print(knapsack(wt,val,w,n))