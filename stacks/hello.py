class stack:
    def __init__(self):
        self.arr=[]

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        self.arr.pop(-1)

    def peek(self):
        return self.arr[-1]

    def display(self):
        for i in self.arr:
            print(i,end=" ")

    def sol(self):
        n=len(self.arr)
        mid=n//2
        c=0
        stk=[]
        for i in range(n):
            c+=1
            if c==mid+1:
                self.arr.pop()
            else:
                stk.append(self.arr.pop())
        return stk[::-1]





if __name__ == '__main__':
    st = stack()
    st.push('1')
    st.push('2')
    st.push('3')
    st.push('4')
    st.push('5')
    st.push('6')
    st.push('7')
    st.display()
    print(st.sol())
