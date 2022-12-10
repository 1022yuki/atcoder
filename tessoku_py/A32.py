N, A, B = map(int, input().split())

dp = [None]*(N+1)

for i in range(0, N+1):
  if i-A>=0 and dp[i-A] == False:
    dp[i] = True
  elif i-B>=0 and dp[i-B] == False:
    dp[i] = True
  else:
    dp[i] = False

# print(dp)

if dp[N]:
  print('First')
else:
  print('Second')