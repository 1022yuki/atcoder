S = input()
T = input()

dp = []
for i in range(len(S)+1):
  dp.append([0]*(len(T)+1))

for i in range(len(S)+1):
  for j in range(len(T)+1):
    if i!=0:
      dp[i][j] = max(dp[i][j], dp[i-1][j])
    if j!=0:
      dp[i][j] = max(dp[i][j], dp[i][j-1])
    if i!=0 and j!=0:
      if S[i-1] != T[j-1]:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1])
      if S[i-1] == T[j-1]:
        dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

# print(dp)
print(dp[len(S)][len(T)])