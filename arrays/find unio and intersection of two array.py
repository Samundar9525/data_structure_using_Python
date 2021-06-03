def union(a,n,b,m):
    i = 0
    j = 0
    ma = 0
    uni=[]
    int=[]
    while i < n  and j < m :
        if a[i] < b[j]:
            if a[i] not in uni:
                uni.append(a[i])
            i += 1
        elif a[i] == b[j]:
            if a[i] not in int:
                int.append(a[i])
                ma = ma + 1
            i += 1
            j += 1
        else:
            if b[j] not in uni:
                uni.append(b[j])
            j += 1

    # bacha hua element ke liye yee wextra w2ork kiya gaya hai

    while i<n:
        if a[i] not in uni:
            uni.append(a[i])
        i += 1

    while j<m:
        if b[j] not in uni:
            uni.append(b[j])
        j += 1

    # t = a + b
    # c = 0
    # dic = {}
    # tot=n+m
    # for i in range (tot):
    #     if t[i] not in dic:
    #         uni.append(t[i])
    #         c+=1
    #         dic[t[i]]=1




    print("Union : ",uni," total element in union  : ")
    print("Intersection : ",int,"         total element in intersection  : ",ma)
    return 0


if __name__ == '__main__':
    a=[1,1,2,2,3,3,7]
    b=[6,7,7]

    # a=[1,2,3,4,5]
    # b=[3,4,5,6,7,8]


    # a=[3,3,3,3]
    # b=[3,3,3,3,3,3,3,3]
    (union(a,len(a),b,len(b)))