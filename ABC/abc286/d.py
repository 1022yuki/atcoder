N, X = map(int, input().split())
A = []
B = []
for i in range(N):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)

dp = []
for i in range(N+1):
  dp.append([False]*(X+1))
dp[0][0] = True

for i in range(N):
  a = A[i]
  b = B[i]
  for sum in range(X+1):
    if not dp[i][sum]:
      continue
    # print(i, sum)
    for num in range(b+1):
      if sum+a*num <= X:
        dp[i+1][sum+a*num] = True

# print(dp)
if dp[N][X]:
  print('Yes')
else:
  print('No')