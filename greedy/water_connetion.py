class node:
    def __init__(self, data):
        self.data = data
        self.next = None
def sol(a,b,c):
    di={}
    for i in range(len(a)):
        p=a[i]
        q=b[i]
        r=c[i]
        if p not in di:
            te=node(p)
            di[p]=te
            te.next=node(q)
    print(di)

if __name__ == '__main__':
    s=[7,5,4,2,9,3]
    d=[4,9,6,8,7,1]
    w=[98,72,10,22,17,66]

    print(sol(s,d,w))
