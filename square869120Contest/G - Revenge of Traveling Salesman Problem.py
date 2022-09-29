N, M = map(int, input().split())

ALL = 1<<N
inf = 10**100

dist = []
for i in range(N):
  dist.append([inf]*N)
for i in range(N):
  dist[i][i] = 0

# time[i]は封鎖される時間、道を記録する配列
time = []
for i in range(N):
  time.append([inf]*N)

for i in range(M):
  s, t, d, ti = map(int, input().split())
  dist[s-1][t-1] = d
  dist[t-1][s-1] = d
  time[s-1][t-1] = ti
  time[t-1][s-1] = ti

# bitDPの最短時間を管理する配列
cost = []
for i in range(ALL):
  cost.append([inf]*N)
cost[0][0] = 0

# bitDPの最短時間を達成する方法の総数を管理する配列
num = []
for i in range(ALL):
  num.append([0]*N)
num[0][0] = 1

# print(cost)

def has_bit(n, i):
  return n & (1<<i) > 0

for n in range(ALL):
  for i in range(N):
    for j in range(N):
      if has_bit(n, j) or i==j:
        continue
      # time関連の処理
      if cost[n][i]+dist[i][j] > time[i][j]:
        continue
      # cost, numの処理
      if cost[n|(1<<j)][j] > cost[n][i] + dist[i][j]:
        num[n|(1<<j)][j] = num[n][i]
      if cost[n|(1<<j)][j] == cost[n][i] + dist[i][j]:
        num[n|(1<<j)][j] += num[n][i]
      cost[n|(1<<j)][j] = min(cost[n|(1<<j)][j], cost[n][i] + dist[i][j])

# print(cost)
ans_dist = cost[ALL-1][0]
ans_comb = num[ALL-1][0]
# print(ans_dist)
# print(ans_comb)

if ans_dist == inf:
  print('IMPOSSIBLE')
else:
  print(ans_dist, ans_comb)