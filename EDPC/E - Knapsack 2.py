N, W = map(int, input().split())

wl = []
vl = []

for i in range(0, N):
  w, v = map(int, input().split())
  wl.append(w)
  vl.append(v)

s = sum(vl)

# dp[i][v]: 品物1~iからいくつか選んで価値の合計がvであるときの重さの合計の最小値
dp = []
for i in range(N+1):
  dp.append([10**20]*(s+1))

dp[0][0] = 0

# print(dp)

for i in range(1, N+1):
  for j in range(s+1):

    # 品物iを選ばない場合
    weight = dp[i-1][j]
    dp[i][j] = min(weight, dp[i][j])

    # 選ぶ場合
    if j >= vl[i-1] :
      weight = dp[i-1][j-vl[i-1]] + wl[i-1]
      if weight <= W:
        dp[i][j] = min(weight, dp[i][j])

# print(dp)

for i in range(s, -1, -1):
  # print(i)
  if dp[N][i] <= 10**11:
    ans = i
    break

print(ans)