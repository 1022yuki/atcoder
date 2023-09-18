N, M = map(int, input().split())

X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

P = []
Q = []
for i in range(M):
  p, q = map(int, input().split())
  P.append(p)
  Q.append(q)

def dist(x1, y1, x2, y2):
  return((x1-x2)**2+(y1-y2)**2)**0.5

inf = 10**10
dp = []
for i in range(1<<(N+M+1)):
  dp.append([-inf]*(N+M+1))

dp[0][0] = 0

