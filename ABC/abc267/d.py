N, M = map(int, input().split())
A = list(map(int,input().split()))

inf = -10**100
# dp[i][m]: 配列Aのi番目まで見て、それまでにm個選んでいる場合のi×Biの最大値
dp = []
for i in range(N+1):
  dp.append([inf]*(M+1))

for i in range(1,N+1):
  dp[i][1] = A[i-1]

# print(dp)

for i in range(1,N):
  for m in range(1, M+1):
    # dp[i][m]からの遷移を考える
   
    # i+1番目の数字を選ばないとき
    dp[i+1][m] = max(dp[i+1][m], dp[i][m])

    # i+1番目の数字を選ぶとき
    if m < M:
      dp[i+1][m+1] = max(dp[i+1][m+1], dp[i][m] + (m+1) * A[i])

# print(dp)
ans = dp[N][M]
print(ans)