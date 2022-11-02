N = int(input())

grid = []
sum_grid = []
for i in range(1501):
  grid.append([0]*1501)
for i in range(1502):
  sum_grid.append([0]*1502)

# print(grid)

for i in range(N):
  A, B, C, D = map(int, input().split())
  grid[A][B] += 1
  grid[C][B] -= 1
  grid[A][D] -= 1
  grid[C][D] += 1

for i in range(1, 1502):
  for j in range(1, 1502):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

for j in range(1, 1502):
  for i in range(1, 1502):
    sum_grid[i][j] = sum_grid[i][j] + sum_grid[i-1][j]


ans = 0
for i in range(1, 1502):
  for j in range(1, 1502):
    if sum_grid[i][j] >= 1:
      ans += 1

print(ans)