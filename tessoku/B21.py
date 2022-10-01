N = int(input())
S = input()

# dp[l][r]: 文字列のl文字目からr文字目までが範囲になっている時、既に最大何文字を回文として追加できているか

dp = []
for i in range(N+1):
  dp.append([-10]*(N+1))

for i in range(1, N+1):
  dp[i][i] = 1
  if S[i] == S[i+1]:
    dp[i][i+1] = 2

for len in range(2, N+1):
  for l in range(1, N+1):
    r = l + len - 1
    # l=1, r=2 からスタート