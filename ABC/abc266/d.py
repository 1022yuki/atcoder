N = int(input())

# 配列T: 時刻tに座標xを訪れるともらえる得点
T = []
for i in range(10**5 + 1):
  T.append([0]*5)

for i in range(N):
  t, x, a = map(int, input().split())
  T[t][x] = a

# print(T)

# dp[t][x]: 時刻tに座標xにいるとき、捕まえることができるすぬけ君の大きさの合計の最大値
dp = []
for i in range(10**5 + 1):
  dp.append([-10**10]*5)
dp[0][0] = 0

# print(dp)

for t in range(1, 10**5+1):
  for x in range(5):
    dp[t][x] = max(dp[t][x], dp[t-1][x] + T[t][x])
    if x != 0:
      dp[t][x] = max(dp[t][x], dp[t-1][x-1] + T[t][x])
    if x != 4:
      dp[t][x] = max(dp[t][x], dp[t-1][x+1] + T[t][x])

print(max(dp[10**5]))