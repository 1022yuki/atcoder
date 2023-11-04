N = int(input())
P = list(map(int, input().split()))

# 1回参加した時のレートで初期化
maxRate = max(P)-1200

# dp[k][i]: k回参加して、1番最後に参加したコンテストがi番目までの時の分子の最大値
dp = []
for k in range(N+1):
  dp.append([-1]*N)

dp[1][0] = P[0]
for j in range(1, N):
  dp[1][j] = max(dp[1][j-1], P[j])


for k in range(2, N+1):
  for j in range(k-1, N):
    dp[k][j] = max(dp[k][j-1], (dp[k-1][j-1])*0.9+P[j])

bunbo = [-1]*(N+1)
bunbo[1] = 1
for k in range(2, N+1):
  bunbo[k] = bunbo[k-1]*(0.9)+1

for k in range(1, N+1):
  maxRate = max(maxRate, dp[k][N-1]/bunbo[k] - 1200/(k**0.5))

print(maxRate)