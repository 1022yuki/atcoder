S = list(input())
ls = len(S)

S = [''] + S
mod = 998244353

print(S)

dp = []
for i in range(ls+1):
    dp.append([0]*(ls+1))

dp[0][0] = 1

for i in range(1, ls+1):
    for j in range(ls+1):
        if S[i]=='(':
          if j>0:
            dp[i][j] += max(0, dp[i-1][j-1])
            dp[i][j] %= mod
        elif S[i]==')':
          if j+1<=ls:
            dp[i][j] += max(0, dp[i-1][j+1])
            dp[i][j] %= mod
        else:
          #  '('にする場合
          if j>0:
            dp[i][j] += max(0, dp[i-1][j-1])
          #  ')' にする場合
          if j+1<=ls:
            dp[i][j] += max(0, dp[i-1][j+1])
          dp[i][j] %= mod

# print(dp)
print(dp[ls][0])