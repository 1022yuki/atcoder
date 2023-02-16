S = input()
T = input()

dp = []
for i in range(len(S)+1):
  dp.append([10**10]*(len(T)+1))

for i in range(len(S)+1):
  for j in range(len(T)+1):
    if i == 0:
      dp[i][j] = j
    elif j == 0:
      dp[i][j] = i
    else:
      if S[i-1]==T[j-1]:
        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1])
      else:
        dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)

# print(dp)
print(dp[len(S)][len(T)])