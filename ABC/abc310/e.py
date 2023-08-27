N = int(input())
S = list(input())

dp = []
for i in range(2):
    dp.append([0]*(N+1))


ans = 0

dp[int(S[0])][1] = 1
ans += dp[1][1]

for j in range(2, N+1):
    num_j = int(S[j-1])

    if num_j == 0:
      dp[0][j] = 1
      dp[1][j] = j-1

    if num_j == 1:
      dp[0][j] = dp[1][j-1]
      dp[1][j] = dp[0][j-1]+1
    
    ans += dp[1][j]

# print(dp)
print(ans)