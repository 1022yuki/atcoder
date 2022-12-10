N, S = map(int, input().split())
A = [0]+list(map(int, input().split()))

dp = []
for i in range(N+1):
  dp.append([False]*(S+1))

dp[0][0] = True

for i in range(N):
  for j in range(S+1):
    if dp[i][j]:
      dp[i+1][j] = True
      if j+A[i+1] <= S:
        dp[i+1][j+A[i+1]] = True


if not dp[N][S]:
  print(-1)
  exit()

sum = S
card = N
ans = []

while True:
  if card == 0:
    break
  if sum-A[card]>=0 and dp[card-1][sum-A[card]]:
    ans.append(card)
    sum -= A[card]
  card -= 1

ans.reverse()

print(len(ans))
print(*ans)