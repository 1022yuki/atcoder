H, W = map(int, input().split())
grid = []
for i in range(H):
  grid.append(list(map(int, input().split())))
Q = int(input())
edges = []
for i in range(Q):
  a, b, c, d = map(int, input().split())
  edges.append([a, b, c, d])

sum_grid = []
for i in range(H+1):
  sum_grid.append([0]*(W+1))

# 横方向累積和
for i in range(1, H+1):
  for j in range(1, W+1):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

# 縦方向累積和
for j in range(1, W+1):
  for i in range(1, H+1):
    sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j]

for a, b, c, d in edges:
  ans = sum_grid[c][d]-sum_grid[c][b-1]-sum_grid[a-1][d] + sum_grid[a-1][b-1]
  print(ans)