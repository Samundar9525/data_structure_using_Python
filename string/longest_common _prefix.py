def compare(str1,str2):
    i=0
    tem=''
    while(i<len(str1) and i<len(str2)):
        if str1[i]==str2[i]:
            tem+=str1[i]
        i+=1
    return tem

def sol(arr):
    n=len(arr)
    if n==1:
        if arr[0]=='':
            return '""'
        else:
            return arr[0]
    else:
        te=''
        te=compare(arr[0],arr[1])

        for i in range(2,n):
            te=compare(te,arr[i])
    if len(te)<1:
        return '""'
    else:
        return te

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(sol(strs))
