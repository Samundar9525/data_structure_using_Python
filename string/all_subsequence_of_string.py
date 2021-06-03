dic=[]

def subseq(inp,out):
    if (len(inp)<=0):
        if len(out)!=0:
            dic.append(out)  
        return
    
    p=subseq(inp[1:],out+inp[0])
    n=subseq(inp[1:],out)
    
st='abcd'
subseq(st,'')
dic.sort()

print((dic))
