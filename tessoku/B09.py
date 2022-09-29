N = int(input())

ind = []
for i in range(N):
  inp = list(map(int, input().split()))
  ind.append(inp)

grid = []
for i in range(1501):
  grid.append([0]*1501)

for a, b, c, d in ind:
  grid[a][b] += 1
  grid[a][d] -= 1
  grid[c][b] -= 1
  grid[c][d] += 1

sum_grid = []
for i in range(1502):
  sum_grid.append([0]*1502)

for i in range(1, 1502):
  for j in range(1, 1502):
    sum_grid[i][j] = sum_grid[i][j-1] + grid[i-1][j-1]

for j in range(1, 1502):
  for i in range(1, 1502):
    sum_grid[i][j] += sum_grid[i-1][j]

# for i in range(5):
#   print(sum_grid[i][:5])

ans = 0
for i in range(1502):
  for j in range(1502):
    if sum_grid[i][j] != 0:
      ans += 1

print(ans)