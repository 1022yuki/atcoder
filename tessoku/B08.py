N = int(input())

grid = []
for i in range(1500):
  grid.append([0]*1500)
for i in range(N):
  x, y = map(int, input().split())
  grid[x-1][y-1] += 1

# print(grid)

sum_grid = []
for i in range(1501):
  sum_grid.append([0]*1501)

# 横方向累積和
for i in range(1, 1501):
  for j in range(1, 1501):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

# 縦方向累積和
for j in range(1, 1501):
  for i in range(1, 1501):
    sum_grid[i][j] = sum_grid[i-1][j] + sum_grid[i][j]

# print(sum_grid)

Q = int(input())
queries = []
for i in range(Q):
  a, b, c, d = map(int,input().split())
  queries.append([a, b, c, d])

for a, b, c, d in queries:
  ans = sum_grid[c][d] - sum_grid[a-1][d] -sum_grid[c][b-1] + sum_grid[a-1][b-1]
  print(ans)