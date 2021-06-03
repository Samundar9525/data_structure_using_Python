import itertools

def sub(s,n):
    return list(itertools.combinations(s,n))
if __name__ == '__main__':
    s=["a","b","c",'d']
    a=[]
    for i in range (len(s)):
        a.append((sub(s,i)))
    for j in a:
        for k in j:
            print(k)
    
    
