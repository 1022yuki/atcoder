N, W = map(int, input().split())

item = []
for i in range(N):
  item.append(list(map(int, input().split())))

# print(item)

dp = []
for i in range(N+1):
  dp.append([-10]*(W+1))
dp[0][0] = 0

for i in range(1, N+1):
  for j in range(W+1):
    # 品物iを選ばない
    dp[i][j] = max(dp[i][j], dp[i-1][j])
    # 品物iを選ぶ
    if j-item[i-1][0]>=0:
      dp[i][j] = max(dp[i][j], dp[i-1][j-item[i-1][0]]+item[i-1][1])

# print(dp[N])

ans = 0
for j in range(W+1):
  ans = max(ans, dp[N][j])

print(ans)