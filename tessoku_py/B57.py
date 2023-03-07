N, K = map(int, input().split())

dp = []
li = []
for i in range(N+1):
  li.append(i)
dp.append(li)
for i in range(29):
  dp.append([0]*(N+1))

# print(dp)

def culc(n):
  st_n = str(n)
  lg = len(st_n)
  sum = 0
  for i in range(lg):
    sum += int(st_n[i])
  return n-sum

for i in range(N+1):
  dp[0][i] = culc(dp[0][i])

# print(dp)

for i in range(1, 30):
  for j in range(1, N+1):
    dp[i][j] = dp[i-1][dp[i-1][j]]

# print(dp)

def has_bit(n, i):
  return n&(1<<i) > 0

for n in range(1, N+1):
  c_place = n
  for b in range(30):
    if has_bit(K, b):
      c_place = dp[b][c_place]
  print(c_place)