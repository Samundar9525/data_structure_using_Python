def safe(board,r ,c):
    for i in range (c):
        if (board[r][i])==1:                # ye check karega ki coloum mein aur Queen
            return False                    #   hai ki nahi agar hai toh retun false

    row=r
    col=c
    while(row>=0 and col >=0):
        if (board[row][col]==1):
            return False

        row-=1
        col-=1

    row = r
    col = c
    while (row <n and col >= 0):
        if (board[row][col] == 1):
            return False

        row += 1
        col -= 1
    return True

def printsol(board):
    for i in range (n):
        for j in range (n):
            print(board[i][j],end=" ")
        print(" ")

def solve():
    board=[[0 for i in range (n) ] for j in range (n)]

    if (solveutil(board,0)==False):
        print("Solution Does Not Exist")
        return False
    else:
        printsol(board)

def solveutil(board,coloum):
    if coloum >=n:
        return True
    for i in range (n):
        if (safe (board,i,coloum)==True):
            board[i][coloum]=1
            if solveutil(board,coloum+1)==True:
                return True
            board[i][coloum]=0
    return False

if __name__ == '__main__':
    n=int(input("Enter the size of Board : "))
    solve()


