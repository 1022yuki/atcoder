N = int(input())

grid = []
for i in range(100):
  grid.append([False]*100)

for i in range(N):
  a, b, c, d = map(int, input().split())
  for j in range(a, b):
    for k in range(c, d):
      grid[j][k] = True

ans = 0
for i in range(100):
  for j in range(100):
    if grid[i][j]:
      ans += 1

print(ans)