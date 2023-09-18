N, M = map(int, input().split())

mod = 998244353

dp = []
for i in range(2):
    dp.append([0]*N)
dp[0][0] = 1

for j in range(1, N):
    dp[0][j] += dp[1][j-1]
    dp[1][j] += dp[0][j-1]*(M-1)
    dp[1][j] += dp[1][j-1]*(M-2)
    dp[0][j] %= mod
    dp[1][j] %= mod

ans = (dp[1][N-1]*M)%mod
print(ans)