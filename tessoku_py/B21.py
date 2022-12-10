N = int(input())
S = input()

dp = []
for i in range(N):
  dp.append([0]*N)

for i in range(N):
  dp[i][i] = 1
for i in range(N-1):
  if S[i] == S[i+1]:
    dp[i][i+1] = 2

for len in range(1, N+1):
  for l in range(N-len):
    r = l + len
    # print(l, r)
    if S[l] == S[r]:
      dp[l][r] = max(dp[l+1][r-1]+2, dp[l+1][r], dp[l][r-1])
    else:
      dp[l][r] = max(dp[l+1][r], dp[l][r-1])

# print(dp)
print(dp[0][N-1])