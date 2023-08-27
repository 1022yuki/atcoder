N = int(input())
X = [0]
Y = [0]
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

inf = 10**10

dp = []
for i in range(2):
    dp.append([-1*inf] * (N+1))

dp[0][0] = 0

for i in range(1, N+1):
    if X[i] == 0:
        # 食べない
        dp[0][i] = max(dp[0][i], dp[0][i-1])
        dp[1][i] = max(dp[1][i], dp[1][i-1])
        # 食べる
        dp[0][i] = max(dp[0][i], dp[0][i-1]+Y[i])
        dp[0][i] = max(dp[0][i], dp[1][i-1]+Y[i])
    else:
        # 食べない
        dp[0][i] = max(dp[0][i], dp[0][i-1])
        dp[1][i] = max(dp[1][i], dp[1][i-1])
        # 食べる
        dp[1][i] = max(dp[1][i], dp[0][i-1]+Y[i])

# print(dp)
print(max(dp[0][N], dp[1][N]))