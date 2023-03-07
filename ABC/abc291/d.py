N = int(input())

A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

dp = []
for i in range(2):
  dp.append([0]*N)

dp[0][0] = 1
dp[1][0] = 1

mod = 998244353

for i in range(N-1):
  if A[i+1] != A[i]:
    dp[0][i+1] += dp[0][i]
    dp[0][i+1] %= mod
  if A[i+1] != B[i]:
    dp[0][i+1] += dp[1][i]
    dp[0][i+1] %= mod
  if B[i+1] != A[i]:
    dp[1][i+1] += dp[0][i]
    dp[1][i+1] %= mod
  if B[i+1] != B[i]:
    dp[1][i+1] += dp[1][i]
    dp[1][i+1] %= mod

print((dp[0][N-1]+dp[1][N-1])%mod)