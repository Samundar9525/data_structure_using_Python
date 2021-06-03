def sol(arr,res):
    if len(arr)==0:
        return res
    res.append(arr.pop(-1))
    sol(arr,res)

if __name__ == '__main__':
    arr=[1,2,3,4]
    res=[]
    sol(arr,res)
    print(res)