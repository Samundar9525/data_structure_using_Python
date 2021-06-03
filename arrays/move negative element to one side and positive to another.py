def arrange(arr):
    l=0
    r=len(arr)-1

    while(l<=r):
        if arr[l]<0 and arr[r]>0:
            l+=1;r-=1
        elif arr[l]<0 and arr[r]<0:
            l+=1
        elif arr[l]>0 and arr[r]<0:
            arr[l],arr[r]=arr[r],arr[l]
            l+=1;r-=1
        elif arr[l]>0 and arr[r]>0:
            r-=1







if __name__ == '__main__':
    arr=[3,-5,4,-8,6,7,-4,-1,-4,9,11,-15,7,-19,16,-15]
    print(arr)
    arrange(arr)
    print(arr)