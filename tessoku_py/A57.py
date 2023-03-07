N, Q = map(int, input().split())
A = [0]+list(map(int, input().split()))

qs = []
for i in range(Q):
  x, y = map(int, input().split())
  qs.append([x, y])

dp = []
for i in range(30):
  dp.append([None]*(N+1))

for i in range(30):
  for j in range(1, N+1):
    if i==0:
      dp[i][j] = A[j]
    else:
      nj = dp[i-1][j]
      dp[i][j] = dp[i-1][nj]

# print(dp)

def has_bit(n, i):
  return n&(1<<i)>0

for i in range(Q):
  q = qs[i]
  c_place = q[0]
  day = q[1]
  for b in range(30):
    if has_bit(day, b):
      c_place = dp[b][c_place]
  print(c_place)