N, M = map(int, input().split())

grid = []
for i in range(N):
    s = input()
    grid.append(s)

import sys
sys.setrecursionlimit(10**9)

st_set = set()

visited = []
for i in range(N):
    visited.append([False]*M)

def dfs(i, j):
    st_set.add((i, j))
    visited[i][j] = True
    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni = i + di
        nj = j + dj
        if grid[ni][nj] == '#':
            continue
        while True:
            visited[ni][nj] = True
            if grid[ni+di][nj+dj] == '#':
                break
            ni += di
            nj += dj

        # print(ni, nj)
        if not (ni, nj) in st_set:
            dfs(ni, nj)

dfs(1, 1)
# print(visited)

ans = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            ans += 1
print(ans)