N, M = map(int, input().split())

grid = []
for i in range(N):
    inp = list(input())
    grid.append(inp)

for i in range(N):
    for j in range(M):
        if i!=0:
            if grid[i-1][j]=='#':
                grid[i][j]='#'
            if j!=0:
                if grid[i-1][j-1]=='#':
                    grid[i][j]='#'

print(grid)

