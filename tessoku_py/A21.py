N = int(input())

P = []
A = []
for i in range(N):
  p, a = map(int, input().split())
  P.append(p)
  A.append(a)

# dp[l,r]: l番目からr番目のブロックが残っている時の得点の最大値
# 求めるものはi=1~Nで、dp[i][i]の最大値
dp = []
for i in range(N+1):
  dp.append([-1]*(N+1))

dp[1][N] = 0

for i in range(1, N+1):
  for j in range(N, i-1, -1):
    # 右から1つとる(j+1番目のブロックが取られる)
    if j != N:
      if i <= P[j] <= j:
        dp[i][j] = max(dp[i][j], dp[i][j+1]+A[j])
      else:
        dp[i][j] = max(dp[i][j], dp[i][j+1])
    # 左から1つとる(i-1番目のブロックが取られる)
    if i != 1:
      if i <= P[i-2] <= j:
        dp[i][j] = max(dp[i][j], dp[i-1][j]+A[i-2])
      else:
        dp[i][j] = max(dp[i][j], dp[i-1][j])

ans = 0
for i in range(1, N+1):
  ans = max(ans, dp[i][i])
print(ans)