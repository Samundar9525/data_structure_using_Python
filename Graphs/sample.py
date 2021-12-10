row = len(grid)
col = len(grid[0])
que = []
time = 0


def find(i, j, c):
    x = [-1, 1, 0, 0]
    y = [0, 0, -1, 1]
    for p in range(4):
        if i + x[p] < 0 or j + y[p] < 0 or i + x[p] >= row or j + y[p] >= col or grid[i + x[p]][j + y[p]] != 1:
            continue
        else:
            c[0] += 1
            que.append([i + x[p], j + y[p]])
            grid[i + x[p]][j + y[p]] = 2


for i in range(row):
    for j in range(col):
        if grid[i][j] == 2:
            que.append([i, j])
c = [len(que)]
while (c[0] > 0):

    for i in range(c[0]):
        p = que.pop(0)
        c[0] -= 1
        find(p[0], p[1], c)
    #  c=len(que)
    if (c[0] > 0):
        time += 1

for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            return -1
return time