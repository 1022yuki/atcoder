H, W = map(int, input().split())
grid = []
for i in range(H):
  inp = input()
  grid.append(inp)

dp = []
for i in range(H):
  dp.append([0]*W)

dp[0][0] = 1

for i in range(H):
  for j in range(W):
    if grid[i][j] == '#':
      continue
    if i != H-1:
      dp[i+1][j] += dp[i][j]
    if j != W-1:
      dp[i][j+1] += dp[i][j]

print(dp[H-1][W-1])