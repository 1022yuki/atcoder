from collections import deque

H, W = map(int, input().split())
grid = []
for i in range(H):
    inp = list(input())
    grid.append(inp)

# print(grid)

# >をチェック
for i in range(H):
    flag = False
    for j in range(W):
        if flag:
            if grid[i][j]==".":
                grid[i][j] = "#1"
            else:
                flag = False
        if grid[i][j]==">":
            flag = True

# <をチェック
for i in range(H):
    flag = False
    for j in range(W-1, -1, -1):
        if flag:
            if grid[i][j]==".":
                grid[i][j] = "#2"
            elif grid[i][j]=="#1":
                grid[i][j] = "#2"
            else:
                flag = False
        if grid[i][j]=="<":
            flag = True

# vをチェック
for j in range(W):
    flag = False
    for i in range(H):
        if flag:
            if grid[i][j]==".":
                grid[i][j] = "#3"
            elif grid[i][j]=="#1":
                grid[i][j] = "#3"
            elif grid[i][j]=="#2":
                grid[i][j] = "#3"
            else:
                flag = False
        if grid[i][j]=="v":
            flag = True

# ^をチェック
for j in range(W):
    flag = False
    for i in range(H-1, -1, -1):
        if flag:
            if grid[i][j]==".":
                grid[i][j] = "#4"
            elif grid[i][j]=="#1":
                grid[i][j] = "#4"
            elif grid[i][j]=="#2":
                grid[i][j] = "#4"
            elif grid[i][j]=="#3":
                grid[i][j] = "#4"
            else:
                flag = False
        if grid[i][j]=="^":
            flag = True

# print(grid)

for i in range(H):
    for j in range(W):
        if grid[i][j]=="#" or grid[i][j]=="#1" or grid[i][j]=="#2" or grid[i][j]=="#3" or grid[i][j]=="#4" or grid[i][j]==">" or grid[i][j]=="<" or grid[i][j]=="v" or grid[i][j]=="^":
            grid[i][j] = "#"
        if grid[i][j]=="S":
            start = (i, j)
        if grid[i][j]=="G":
            goal = (i, j)

# print(grid)

Q = deque()
Q.append(start)
# print(Q)

dist = []
for i in range(H):
    dist.append([-1]*W)
dist[start[0]][start[1]] = 0

while len(Q)>0:
    i, j = Q.popleft()
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not(0<=i2<H and 0<=j2<W):
            continue
        if grid[i2][j2]=="#":
            continue
        if dist[i2][j2]==-1:       
          dist[i2][j2] = dist[i][j]+1
          Q.append([i2, j2])

print(dist[goal[0]][goal[1]])