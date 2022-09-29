N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = []
for i in range(N+1):
  dp.append([False]*(S+1))

dp[0][0] = True

for i in range(N):
  for j in range(S+1):
    if dp[i][j]:
      dp[i+1][j] = True
      if j+A[i] <= S:
        dp[i+1][j+A[i]] = True


if not dp[N][S]:
  print(-1)
  exit()

ans = []
card = N
sum = S

# while True:
#   if card == 0:
#     break
#   if sum-A[card-1] >= 0 and dp[card-1][sum-A[card-1]]:
#     ans.append(card)
#     sum -= A[card-1]
#     card -= 1
#   else:
#     card -= 1

while True:
  if card == 0:
    break
  if dp[card-1][sum]:
    card -= 1
  else:
    ans.append(card)
    sum -= A[card-1]
    card -= 1

ans.reverse()
# print(ans)
# print(card)
# print(sum)

print(len(ans))
print(*ans)