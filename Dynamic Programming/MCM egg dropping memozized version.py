import sys
def display(arr):
    for i in (arr):
        for j in i :
            print(j,end=" ")
        print("")

def eggdrop(egg,floor):
    if floor==0 or floor==1:
        return floor
    if egg==1:
        return floor

    if t[egg][floor]!=-1:
        return t[egg][floor]

    res=99999999
    for k in range (1,floor+1):
        if t[egg-1][k-1]!=-1:
            low=t[egg-1][k-1]
        else:
            low=eggdrop(egg-1,k-1)
            t[egg-1][k-1]=low

        if t[egg][floor - k] != -1:
            high= t[egg][floor - k]
        else:
            high = eggdrop(egg,floor-k)
            t[egg][floor - k] =high

        temp=max(low,high)+1

        if temp<res:
            res=temp        # yahan par binary search use karo
            t[egg][floor]=res
    return t[egg][floor]

if __name__ == '__main__':
    egg=2
    floor=10           #iska output 4 aana mangta hai
    t=[[-1 for i in range (floor+1)]  for j in range (egg+1)]
    print("minimum number of trial : ",eggdrop(egg,floor))
    #display(t)