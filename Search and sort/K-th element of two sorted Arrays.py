def sol(arr1, arr2, n, m, k):
    st = 0
    en = 0
    c = 0
    flag = 0
    temp = []
    while (st < n and en < m):
        if arr1[st] < arr2[en]:
            temp.append(arr1[st])
            st += 1
            c += 1
        elif arr1[st] > arr2[en]:
            temp.append(arr2[en])
            en += 1
            c += 1
        else:
            temp.append(arr1[st])
            st += 1
            c += 1
            if c == k:
                flag = 1
                break
            temp.append(arr2[en])
            en += 1
            c += 1
            if c == k:
                flag = 1
                break
        if c == k:
            flag = 1
            break
    if flag == 0:
        while (st < n):
            temp.append(arr1[st])
            st += 1
            c += 1
            if c == k:
                break
        while (en < m):
            temp.append(arr2[en])
            en += 1
            c += 1
            if c == k:
                break

    return (temp[c - 1])

def optimised(arr1, arr2, n, m, k):
    st = 0
    en = 0
    c = 0

    while (st < n and en < m):
        if arr1[st] < arr2[en]:
            st += 1
            c += 1
            if c == k:
                return arr1[st - 1]
        elif arr1[st] > arr2[en]:
            en += 1
            c += 1
            if c == k:
                return arr2[en - 1]
        else:
            st += 1
            c += 1
            if c == k:
                return arr1[st - 1]
            en += 1
            c += 1
            if c == k:
                return arr1[st - 1]

    while (st < n):
        st += 1
        c += 1
        if c == k:
            return arr1[st - 1]
    while (en < m):
        en += 1
        c += 1
        if c == k:
            return arr2[en - 1]


if __name__ == '__main__':
    arr1=[100, 112, 256, 349, 770]
    arr2=[72, 86, 113, 119, 265, 445, 892]
    n=len(arr1)
    m=len(arr2)
    k=7
    print(sol(arr1,arr2,n,m,k))
    print(optimised(arr1,arr2,n,m,k))

