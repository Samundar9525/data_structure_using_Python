def kadane (arr):
    n=len(arr)
    ma=arr[0]
    curr=0
    st=0
    en=0
    flag=0
    for i in range (n):
        curr=curr+arr[i]

        if ma<curr:
            ma=curr
            st=flag
            en=i

        if curr<0:
            curr=0
            flag=i+1

    t.append(ma)
    t.append(st)
    t.append(en)
    return t

if __name__ == '__main__':
    arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4,  2,  1]
    t = []
    print(kadane(arr))
    st=t[1]
    en=t[2]
    print( "subarray : ", arr[st:en+1]  ,"\t\t\t and sum is  :: ",t[0])