N, M, K = map(int, input().split())

# dp[i][j]: 配列Aの最後の要素がjであり、長さiの配列の場合の数
# 最終的に求めたいものはΣdp[N][j]
dp = []
for i in range(0, N):
  dp.append([0]*M)

for j in range(0, M):
  dp[0][j] = 1

# 遷移を考える
for i in range(0, N-1):
  sum = [dp[i][0]]
  # 累積和
  for j in range(0, M-1):
    s = sum[-1]+dp[i][j+1]
    sum.append(s)

  for j in range(0, M):
    if j-K>=0:
      dp[i+1][j] = (dp[i+1][j] + sum[j-K]) % 998244353
    if j+K<=M-1:
      dp[i+1][j] += (sum[-1] - sum[j+K-1]) % 998244353

    # for k in range(0, M):
    #   if k>=j+K or k<=j-K:
    #       dp[i+1][j] += dp[i][k]

ans = 0
for j in range(0, M):
  ans = (ans + dp[N-1][j]) % 998244353

print(ans % 998244353)

# print(dp)