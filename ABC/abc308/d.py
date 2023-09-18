H, W = map(int, input().split())

grid = []
for i in range(H):
    grid.append(list(input()))

import sys
sys.setrecursionlimit(10**9)

st = ['s', 'n', 'u', 'k', 'e']

visited = []
for i in range(H):
    visited.append([False]*W)

def dfs(i, j, now):
    # print(i, j, now)
    if i==H-1 and j==W-1:
        print('Yes')
        exit()
    if now == 's':
        num = 0
    elif now == 'n':
        num = 1
    elif now == 'u':
        num = 2
    elif now == 'k':
        num = 3
    elif now == 'e':
        num = 4
    visited[i][j] = True
    for ni, nj in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if ni<0 or ni>=H or nj<0 or nj>=W:
            continue
        if visited[ni][nj]:
            continue
        if grid[ni][nj] != st[(num+1)%5]:
            continue 
        dfs(ni, nj, st[(num+1)%5])

visited[0][0] = True
dfs(0, 0, 's')
print('No')