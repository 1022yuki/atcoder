N = int(input())

X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

def dist(x1, y1, x2, y2):
  dis = ((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))**0.5
  return dis

def has_bit(n, i):
  return n&(1<<i)>0

inf = 10**9

dp = []
for i in range(2**N):
  app = [inf]*N
  dp.append(app)
dp[0][0] = 0

for n in range(2**N):
  for i in range(N):
    for j in range(N):
      if i == j:
        continue
      if i != 0:
        if not has_bit(n, i):
          continue
      if has_bit(n, j):
        continue
      dis = dist(X[i], Y[i], X[j], Y[j])
      dp[n|(1<<j)][j] = min(dp[n|(1<<j)][j], dp[n][i]+dis)

print(dp[2**N-1][0])