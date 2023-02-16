N = int(input())

city = []
for i in range(N):
  x, y = map(int, input().split())
  city.append([x, y])

def dist(x1, y1, x2, y2):
  dist = ((x1-x2)**2+(y1-y2)**2)**0.5
  return dist

def has_bit(n, i):
  return (n&(1<<i)>0)

inf = 10**10
dp = []
for i in range(1<<N):
  dp.append([inf]*N)

dp[0][0] = 0

for n in range(1<<N):
  for i in range(N):
    if n!=0:
      if not has_bit(n, i):
          continue
    for j in range(N):
      if i==j:
        continue
      if has_bit(n, j):
        continue
      dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i]+dist(city[i][0], city[i][1], city[j][0], city[j][1]))

print(dp[(1<<N)-1][0])