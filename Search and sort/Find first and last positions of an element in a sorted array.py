t=1
for _ in range (t):
    n=[9,5]
    size=n[0]
    pat=n[1]
    arr=[1 ,3, 5, 5 ,5, 5 ,67, 123 ,125]
    st=0
    en=0
    for i in range (size):
        if st==0 and arr[i]==pat:
            st=i
        else:
            if arr[i]==pat:
                en=i
    if st==0 and en==0:
        print(-1)
    else:
        print(st,en)

