H, W = map(int, input().split())

grid = []
for i in range(H):
  s = list(input())
  grid.append(s)

# print(grid)

for i in range(H):
  for j in range(W-1):
    if grid[i][j]=='T' and grid[i][j+1]=='T':
      grid[i][j] = 'P'
      grid[i][j+1] = 'C'

# print(grid)

for i in range(H):
  for j in range(W):
    print(grid[i][j], end='')
  print()