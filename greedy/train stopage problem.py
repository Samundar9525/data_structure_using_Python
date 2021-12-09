def sol(arr,brr):
    n=len(arr)
    i=0
    j=0
    plt=0
    ans=0
    while i<n and j<n:
        if arr[i]<=brr[j]:
            plt+=1
            i+=1
        else:
            plt-=1
            j+=1
        ans=max(ans,plt)
    return ans


if __name__ == '__main__':


    arr=[900, 940, 950, 1100, 1500, 1800]
    brr=[910, 1200, 1120, 1130, 1900, 2000]
    arr.sort()
    brr.sort()

    print(sol(arr,brr))

