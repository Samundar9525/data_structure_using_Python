N=4   # maze ka size.......

def safe(maze,x,y):
    if (x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1):
        return True
    else:
        return False

def printsol(sol):
    for i in range (N):
        for j in range (N):
            print(sol[i][j],end=" ")
        print()


def solveMaze(maze):

    sol=[["." for i in range (N)] for j in range (N)]

    if solveMazeUtil(maze,0,0,sol)==False:
        print("Solution Does not Exists")
        return False
    else:
        printsol(sol)
    return True

def solveMazeUtil(maze,x,y,sol):
    if (x==N-1 and y==N-1 and maze[x][y]==1):
        sol[x][y]=1
        return True        #  ye Apna base case hai jo recursiuon ko end kar dega
    if (safe(maze,x,y)==True):
        sol[x][y]=1

        if solveMazeUtil(maze,x+1,y,sol)==True:
            return True
        if solveMazeUtil(maze,x,y+1,sol)==True:
            return True

        sol[x][y]="." # backtrack yahan pe ho raha hai

        return False







if __name__ == '__main__':
    maze = [[1, 0, 1, 0],
            [1, 1, 1, 1],
            [0, 1, 0, 1],
            [1, 1, 0, 1]]

    # maze = [[1, 1, 1, 1, 1],
    #         [0, 0, 0, 0, 1],
    #         [1, 1, 1, 1, 1],
    #         [1, 0, 0, 0, 0],
    #         [1, 1, 1, 1, 1]]        # yahan par ye kaam nahi kaega

    solveMaze(maze)