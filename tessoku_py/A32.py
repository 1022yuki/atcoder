N, A, B = map(int, input().split())

dp = [False] * (N+1)
# print(dp)
dp[0] = False

for i in range(1, N+1):
  if i>=A and dp[i-A]==False:
    dp[i] = True
  elif i>=B and dp[i-B]==False:
    dp[i] = True
  else:
    dp[i] = False

# print(dp)
if dp[N]:
  print('First')
else:
  print('Second')