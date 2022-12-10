S = input()
T = input()

len_S = len(S)
len_T = len(T)

dp = []
for i in range(len_S+1):
  dp.append([0]*(len_T+1))

for i in range(1, len_S+1):
  for j in range(1, len_T+1):
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    if S[i-1] == T[j-1]:
      dp[i][j] = max(dp[i][j], dp[i-1][j-1]+1)

print(dp[len_S][len_T])