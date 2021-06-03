def eggdrop(egg,floor):

    if floor==0 or floor==1:
        return floor
    if egg==1:
        return floor

    res=99999999

    for k in range (1,floor+1):
        temp=max(eggdrop(egg-1,k-1),eggdrop(egg,floor-k))+1

        if temp<res:
            res=temp
    return res

if __name__ == '__main__':
    egg=2
    floor=10    #iska output 4 aana mangta hai

    print(eggdrop(egg,floor))