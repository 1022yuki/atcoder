N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

Obst = set()
for i in range(M):
  x, y = map(int, input().split())
  Obst.add((x, y))

MOD = 998_244_353

# dp[x][y][z]: (x+A, y+B)の移動をx回、(x+C, y+D)の移動をy回、(x+E, y+F)の移動をz回行った時の移動経路の総和
# 答えはdp[x][y][z](x+y+z=N)の総和
dp = []
for i in range(N+1):
  dp_pre = []
  for j in range(N+1):
    dp_pre.append([0]*(N+1))
  dp.append(dp_pre)
dp[0][0][0] = 1

def CheckObstacle(i, j, k):
  x = A*i+C*j+E*k
  y = B*i+D*j+F*k
  return (x, y) in Obst

for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
      if i+j+k >= N:
        continue
      if CheckObstacle(i, j, k):
        continue
      dp[i+1][j][k] += dp[i][j][k]
      dp[i+1][j][k] %= MOD
      dp[i][j+1][k] += dp[i][j][k]
      dp[i][j+1][k] %= MOD
      dp[i][j][k+1] += dp[i][j][k]
      dp[i][j][k+1] %= MOD

ans = 0
for i in range(N+1):
  for j in range(N+1):
    for k in range(N+1):
      if i+j+k==N and not CheckObstacle(i, j, k):
        ans += dp[i][j][k]
        ans %= MOD

print(ans)