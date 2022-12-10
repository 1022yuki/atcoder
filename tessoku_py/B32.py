N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [False]*(N+1)

for i in range(1, N+1):
  for a in A:
    if i-a>=0 and dp[i-a]==False:
      dp[i] = True

if dp[N]:
  print('First')
else:
  print('Second')