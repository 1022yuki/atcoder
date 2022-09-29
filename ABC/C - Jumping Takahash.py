N, X = map(int, input().split())

A = []
B = []
for i in range(0, N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

# n回のジャンプで座標jにいることができるかどうかを表す配列
# dp[n][j]
dp = []
for i in range(0, N+1):
  dp.append([False]*(X+1))

# print(dp)

dp[0][0] = True

for n in range(0, N):
  for j in range(0, X):
    if dp[n][j]:
      if j+A[n] <= X:
        dp[n+1][j+A[n]] = True
      if j+B[n] <= X:
        dp[n+1][j+B[n]] = True

if dp[N][X]:
  print('Yes')
else:
  print('No')