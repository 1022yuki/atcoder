N = int(input())
S = input()

# dp[0,1][i]: i番目までで0になるもの、1になるものの個数
dp = []
for i in range(2):
    dp.append([0]*(N+1))

ans = 0

for i in range(1, N+1):
    if S[i-1]=='0':
        dp[0][i] = 1
        dp[1][i] = dp[0][i-1]+dp[1][i-1]
    else:
        dp[0][i] = dp[1][i-1]
        dp[1][i] = dp[0][i-1]+1
    ans += dp[1][i]

# print(dp)
print(ans)