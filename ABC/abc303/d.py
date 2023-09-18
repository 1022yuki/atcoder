X, Y, Z = map(int, input().split())
S = input()

lg = len(S)

dp = []
for i in range(2):
    dp.append([10**18]*(lg+1))

dp[0][0] = 0
dp[1][0] = Z


for i in range(1, lg+1):
    if S[i-1]=='a':
        dp[0][i] = min(dp[0][i], dp[0][i-1]+X)
        # dp[0][i] = min(dp[0][i], dp[1][i-1]+Y)
        dp[1][i] = min(dp[1][i], dp[1][i-1]+Y)
        dp[0][i] = min(dp[0][i], dp[1][i-1]+Z+X)
        dp[1][i] = min(dp[1][i], dp[0][i]+Z)
        dp[0][i] = min(dp[0][i], dp[1][i]+Z)
    
    if S[i-1]=='A':
        # dp[1][i] = min(dp[1][i], dp[0][i-1]+Y)
        dp[0][i] = min(dp[0][i], dp[0][i-1]+Y)
        dp[1][i] = min(dp[1][i], dp[1][i-1]+X)
        dp[1][i] = min(dp[1][i], dp[0][i-1]+Z+X)
        dp[0][i] = min(dp[0][i], dp[1][i]+Z)
        dp[1][i] = min(dp[1][i], dp[0][i]+Z)

print(min(dp[0][lg], dp[1][lg]))