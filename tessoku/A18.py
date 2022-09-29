N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(N+1):
  dp.append([False]*(S+1))

# print(dp)

dp[0][0] = True

# 貰うdp
# for i in range(1, N+1):
#   for j in range(S+1):
#     if dp[i-1][j]:
#       dp[i][j] = True
#     if j-A[i-1] >= 0:
#       if dp[i-1][j-A[i-1]]:
#         dp[i][j] = True

# 配るdp
for i in range(N):
  for j in range(S+1):
    if dp[i][j]:
      dp[i+1][j] = True
      if j+A[i] <= S:
        dp[i+1][j+A[i]] = True

print('Yes' if dp[N][S] else 'No')