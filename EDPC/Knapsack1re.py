N, W = map(int, input().split())

wl = []
vl = []

for i in range(0, N):
  w, v = map(int, input().split())
  wl.append(w)
  vl.append(v)

# dp[i][w]: 品物1~iからいくつか選んで重さの合計がwであるときの価値の最大値
dp = []
for i in range(N+1):
  dp.append([-10**10]*(W+1))

dp[0][0] = 0

# print(dp)

for i in range(1, N+1):
  for j in range(W+1):

    # 品物iを選ばない場合
    value = dp[i-1][j]
    dp[i][j] = max(dp[i][j], value)

    # 品物iを選ぶ場合
    if j >= wl[i-1]:
      value = dp[i-1][j-wl[i-1]] + vl[i-1]
      dp[i][j] = max(dp[i][j], value)

ans = max(dp[N])

print(ans)