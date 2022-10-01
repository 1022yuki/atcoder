N, S = map(int, input().split())

card = [(0, 0)]
for i in range(N):
  a, b = map(int, input().split())
  card.append((a, b))

# print(card)

# dp[i][j]: i枚目までのカードを使って総和をjにすることができるか
dp = []
for i in range(N+1):
  dp.append([False]*(S+1))

dp[0][0] = True
# print(dp)

for i in range(1, N+1):
  for j in range(S+1):
    if j-card[i][0] >= 0:
      if dp[i-1][j-card[i][0]]:
        dp[i][j] = True
    if j-card[i][1] >= 0:
      if dp[i-1][j-card[i][1]]:
        dp[i][j] = True

# print(dp)

if dp[N][S]:
  print('Yes')
else:
  print('No')
  exit()

ans = []

now_i = N
now_j = S
while now_i > 0:
  if dp[now_i-1][now_j-card[now_i][0]]:
    ans.append('H')
    now_j -= card[now_i][0]
    now_i -= 1
  else:
    ans.append('T')
    now_j -= card[now_i][1]
    now_i -= 1

# print(now_i, now_j)
# print(ans)

ans.reverse()
# print(ans)

for x in ans:
  print(x, end='')
print()