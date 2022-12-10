N = int(input())

P = []
A = []
for i in range(N):
  p, a = map(int, input().split())
  P.append(p)
  A.append(a)

# dp[l][r]: 左からl個、右からr個取り除いた時の得点
dp = []
for i in range(N+1):
  dp.append([0]*(N+1))

for i in range(N+1):
  for j in range(N-i+1):
    left = 0
    right = 0
    if i != 0:
      left = dp[i-1][j]
      if i+1 <= P[i-1] <= N-j:
        left += A[i-1]
    if j != 0:
      right = dp[i][j-1]
      if i+1 <= P[N-j] <= N-j:
        right += A[N-j]
    dp[i][j] = max(left, right)

ans = 0
for i in range(N+1):
  # print(dp[i][N-i])
  ans = max(ans, dp[i][N-i])

print(ans)