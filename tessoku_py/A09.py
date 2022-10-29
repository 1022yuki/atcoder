H, W, N = map(int, input().split())

rect = []
for i in range(N):
  a, b, c, d = map(int, input().split())
  rect.append([a, b, c, d])

grid = []
sum_grid = []

for i in range(H+1):
  grid.append([0]*(W+1))

for a, b, c, d in rect:
  grid[a-1][b-1] += 1
  grid[a-1][d] -= 1
  grid[c][d] += 1
  grid[c][b-1] -= 1

# print(grid)

for i in range(H+1):
  sum_grid.append([0]*(W+1))

for i in range(1, H+1):
  for j in range(1, W+1):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

for j in range(1, W+1):
  for i in range(1, H+1):
    sum_grid[i][j] += sum_grid[i-1][j]

# print(sum_grid)

for i in range(1, H+1):
  print(*sum_grid[i][1:])