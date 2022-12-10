N, WL = map(int, input().split())

W = []
V = []
for i in range(N):
  w, v = map(int, input().split())
  W.append(w)
  V.append(v)

dp = []
for i in range(N+1):
  dp.append([10**10]*(10**5+1))
dp[0][0] = 0

for i in range(1, N+1):
  for j in range(10**5+1):
    if j-V[i-1]>=0:
      dp[i][j] = min(dp[i-1][j], dp[i-1][j-V[i-1]]+W[i-1])
    else:
      dp[i][j] = dp[i-1][j]

for j in range(10**5, -1, -1):
  if dp[N][j] <= WL:
    print(j)
    exit()