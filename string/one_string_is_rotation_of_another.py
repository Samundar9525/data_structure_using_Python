def solution(str1,str2):
    n=len(str1)
    dic=[]
    for i in range (n):
        temp=str1[n-1]+str1[0:n-1]
        dic.append(temp)
        str1=temp
    print(dic)
    for i in dic:
        if str2==i:
            return True
    return False

def solution2(str1,str2):
    temp=str1+str2
    p=len(str2)
    n=len(temp)
    for i in range (n):
        if temp[i]==str2[0]:
            # print(temp[i:i+p])
            if temp[i:i+p]==str2:
                return  True
    return False


if __name__ == '__main__':
    str1="ABCD"
    str2="BCDA"
    print(solution(str1,str2))
    print(solution2(str1,str2))