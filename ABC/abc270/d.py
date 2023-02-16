N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(2):
  dp.append([0]*(N+1))

# print(dp)

for n in range(N+1):
  for i in range(2):
    for k in range(K):
      if i==0:
        next = 1
      else:
        next = 0
      if n >= A[k]:
        dp[i][n] = max(dp[i][n], n-dp[next][n-A[k]])

print(dp[0][N])