def rev(data):
    return data[::-1]


def loopmethod(data):
    n=len(data)
    t=""
    for i in range(n-1,-1,-1):
        t+=data[i]
    return t
if __name__ == '__main__':
    data=input("Enter A string : ")
    print("original data : ",data)
    # data=rev(data)
    data=loopmethod(data)
    print("After Reverse Data : ",data)
    data=rev(data)
    print("Again Reverse but with short trick : ",data)
