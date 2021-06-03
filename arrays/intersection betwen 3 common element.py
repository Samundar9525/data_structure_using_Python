def sol(a,b,c,n1,n2,n3):
    i=0
    j=0
    k=0
    te=[]
    ue=[]

    while(i<n1 and j<n2 and k<n3):
        if a[i]==b[j]==c[k]:
            if a[i] not in te:
                te.append(a[i])
                ue.append(a[i])
            i+=1
            j+=1
            k+=1
        else:
            if a[i]<b[j]:
                if a[i] not in ue:
                    ue.append(a[i])
                i+=1
            elif b[j]<c[k]:
                if b[j] not in ue:
                    ue.append(b[j])
                j+=1
            else:
                if c[k] not in ue:
                    ue.append(c[k])
                k+=1
    if i<n1:
        if a[i] not in ue:
            ue.append(a[i])
        i += 1
    if j<n2:
        if b[j] not in ue:
            ue.append(b[j])
        j += 1
    if j<n3:
        if c[k] not in ue:
            ue.append(c[k])
        k += 1
    print(te)
    print(ue)


if __name__ == '__main__':
    a=[1, 5, 10, 20, 40, 80]
    b=[6, 7, 10,20, 80, 100]
    c=[3, 4, 15, 20, 30, 70, 80, 120]

    # a = [3,3,3]
    # b = [3,3,3]
    # c = [3,3,3]

    n1=len(a)
    n2=len(b)
    n3=len(c)

    sol(a,b,c,n1,n2,n3)
