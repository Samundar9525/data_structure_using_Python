def sol(arr,n):
    temp=[]
    for i in range(n):
        if arr[i]=='}' or arr[i]==']' or arr[i]==')':
            br=temp.pop()
            print(br)
            if arr[i]=='}' and br!='{':
                return False
            elif arr[i]==']' and br!="[":
                return False
            elif arr[i]==')' and br!='(':
                return False
        else:
            temp.append(arr[i])

    if len(temp)==0:
        return True
    else:
        return False


if __name__ == '__main__':
    str="]"
    arr=list(str)
    print(arr)
    print(sol(arr,len(arr)))