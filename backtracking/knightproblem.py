def safe(board,x,y):
    if (x>=0 and x<n and y>=0 and y<n and board[x][y]==-1):
        return True
    else:
        return False

def printsol(n,board):
    for i in range (n):
        for j in range(n):
            print(board[i][j],end="  ")
        print(" ")


def solve():
    board=[[-1 for i in range (n)] for j in range (n)]

    x_arr=[ 2,1,-1,-2,-2,-1,1,2]                                             #[-2, -2, -1, 1, 2, 2, 1, -1]
    y_arr=[ -1,-2,-2,-1,1,2,2,1]                                            #[1, -1, -2, -2, -1, 1, 2, 2]
    board[0][0] = 0
    pos=1

    if solveutil(board,0,0,x_arr,y_arr,pos)==False:
        print("Not possibble sol")
    else:
        printsol(n,board)


def solveutil(board,x,y,x_arr,y_arr,pos):
    if(pos==(n**2)):
        return True
    for i in range(0,8):
        new_x=x+x_arr[i]
        new_y=y+y_arr[i]
        if safe(board,new_x,new_y):
            board[new_x][new_y] = pos
            if solveutil(board,new_x,new_y,x_arr,y_arr,pos+1)==True:
                return True
            board[new_x][new_y]=-1
    #return False
if __name__=='__main__':
    n = int(input("Enter The size of Chess : "))
    solve()