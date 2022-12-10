N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(N+1):
  dp.append([False]*(S+1))
dp[0][0] = True

for i in range(1, N+1):
  for j in range(S+1):
    if dp[i-1][j]:
      dp[i][j] = True
    if j-A[i-1]>=0 and dp[i-1][j-A[i-1]]:
      dp[i][j] = True

# print(dp)
if dp[N][S]:
  print('Yes')
else:
  print('No')