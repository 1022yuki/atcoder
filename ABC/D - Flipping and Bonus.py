N, M = map(int, input().split())

X = list(map(int, input().split()))

Y = [0]*(N+1)
for i in range(M):
  c, y = map(int, input().split())
  Y[c-1] = y

print(Y)

dp = []
for i in range(N+1):
  dp.append([-(10**10)]*(N+1))

dp[0][0] = 0

# print(dp)

for i in range(N):
  for j in range(0, N+1):
    if j != N:
      omote = dp[i][j] + X[i] + Y[j]
      dp[i+1][j+1] = max(dp[i+1][j+1], omote)
    
    ura = dp[i][j]
    dp[i+1][0] = max(dp[i+1][0], ura)

# print(dp)

print(max(dp[-1]))