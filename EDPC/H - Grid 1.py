H, W = map(int, input().split())
mod = 10**9+7

grid = []
for i in range(H):
  grid.append(input())

# print(grid)

cnt_grid = []
for i in range(H):
  cnt_grid.append([0]*W)

for i in range(H):
  for j in range(W):
    if grid[i][j] == '#':
      cnt_grid[i][j] = 0
    elif i == 0 and j == 0:
      cnt_grid[i][j] = 1
    elif i == 0:
      cnt_grid[i][j] = cnt_grid[i][j-1]
    elif j == 0:
      cnt_grid[i][j] = cnt_grid[i-1][j]
    else:
      cnt_grid[i][j] = (cnt_grid[i-1][j] + cnt_grid[i][j-1])%mod

# print(cnt_grid)

ans = cnt_grid[H-1][W-1]%mod

print(ans)