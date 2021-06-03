def solution(data):
    n=len(data)
    dic={}

    for i in range(n):
        if data[i] not in dic:
            dic[data[i]]=1
        else:
            dic[data[i]]+=1
    for key,val in dic.items():
        if val>1:
            print(key," : ",val)


if __name__ == '__main__':
    st="test string"
    solution(st)