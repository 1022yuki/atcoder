N, W = map(int, input().split())

items = []
for i in range(N):
  w, v = map(int, input().split())
  items.append([w, v])

dp = []
for i in range(N+1):
  dp.append([-10**6]*(W+1))
dp[0][0] = 0

for i in range(N):
  for j in range(W+1):
    # 品物iを選ばない場合
    dp[i+1][j] = max(dp[i+1][j], dp[i][j])
    # 品物iを選ぶ場合
    if j+items[i][0] <= W:
      dp[i+1][j+items[i][0]] = max(dp[i+1][items[i][0]], dp[i][j]+items[i][1])

print(max(dp[N]))