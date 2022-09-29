N = int(input())
pl = list(map(int, input().split()))
sp = sum(pl)

# dp[i][p]: i問目まで問いて得点をp点にできるかどうか、値はboolean
dp = []
for i in range(N+1):
  dp.append([False]*(sp+1))

dp[0][0] = True

# print(dp)

for i in range(1, N+1):
  for j in range(sp+1):

    if dp[i-1][j]:
      dp[i][j] = True
    
    if j-pl[i-1] >= 0:
      if dp[i-1][j-pl[i-1]]:
        dp[i][j] = True

# print(dp)

count = 0
for i in range(sp+1):
  if dp[N][i]:
    count += 1

print(count)