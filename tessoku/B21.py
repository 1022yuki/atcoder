N = int(input())
S = input()

# dp[l][r]: 文字列のl文字目からr文字目までが範囲になっている時、既に最大何文字を回文として追加できているか

dp = []
for i in range(N+1):
  dp.append([-10]*(N+1))

for i in range(N):
  dp[i+1][i+1] = 1
  if i != N-1:
    if S[i] == S[i+1]:
      dp[i+1][i+2] = 2

for len in range(2, N+1):
  for l in range(1, N-len+2):
    r = l + len - 1
    # l=1, r=2 からスタート
    # print(len, l, r)
    if S[l-1] == S[r-1]:
      dp[l][r] = max(dp[l][r], dp[l+1][r], dp[l][r-1], dp[l+1][r-1]+2)
    else:
      dp[l][r] = max(dp[l][r], dp[l+1][r], dp[l][r-1])

# print(dp)

ans = dp[1][N]
print(ans)