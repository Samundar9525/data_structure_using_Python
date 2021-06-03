
def count_substring(str):
    count0=0
    count1=0
    c=0

    for i in str:
        if i=='0':
            count0+=1
        else:               # if i=='1':
            count1+=1

        if count0==count1:
            c+=1
    return c

if __name__ == '__main__':
    str='0111100010'
    res=count_substring(str)
    print(res)