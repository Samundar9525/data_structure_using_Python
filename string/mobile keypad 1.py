def solution(str,dict):

    n=len(str)
    t=''
    for i in range(n):
        val=str[i]
        if val.isspace():
            t+='0'
        else:
            t+=(dict[val])
    return(t)


if __name__ == '__main__':
    al=65
    dict={}
    arr=[2,22,222,
         3,33,333,
         4,44,444,
         5,55,555,
         6,66,666,
         7,77,777,7777,
         8,88,888,
         9,99,999,9999
         ]
    for i in arr:
        dict[chr(al)]=str(i)
        al+=1
    for i,j in dict.items():
        print(i,j)

    str="HELLO WORLD"
    a=solution(str,dict)
    b='4433555555666096667775553'
    if a==b:
        print("YES U DONE IT ")
    else:
        print("kuch toh Gadbad hai daya ")