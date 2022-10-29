N, W = map(int, input().split())

items = []
for i in range(N):
  w, v = map(int, input().split())
  items.append([w, v])

dp = []
for i in range(N+1):
  dp.append([10**10]*(10**5+1))
dp[0][0] = 0

for i in range(1, N+1):
  for j in range(10**5+1):
    # 品物iを使わない場合
    dp[i][j] = min(dp[i][j], dp[i-1][j])
    # 品物iを使う場合
    if j-items[i-1][1] >= 0 and dp[i-1][j-items[i-1][1]]+items[i-1][0] <= W:
      dp[i][j] = min(dp[i][j], dp[i-1][j-items[i-1][1]]+items[i-1][0])

# print(dp)

for i in range(10**5, -1, -1):
  if dp[N][i] < 10**10:
    print(i)
    exit()