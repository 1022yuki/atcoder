N, M = map(int, input().split())

items = []
for i in range(M):
  inp = list(input().split())
  # print(inp)
  join_inp = "".join(inp)
  # print(join_inp)
  items.append(int(join_inp, 2))

# print(items)

inf = 10**10
dp = []
for i in range(M+1):
  dp.append([inf]*(2**N))
dp[0][0] = 0

# print(dp)

def has_bit(n, i):
  return n & 1<<i > 0

for i in range(M):
  for n in range(1<<N):
    # print(i, n)
    # print(dp[i+1][n|items[i]])
    # print('A')
    dp[i+1][n|items[i]] = min(dp[i+1][n|items[i]], dp[i][n]+1)
    dp[i+1][n] = min(dp[i+1][n], dp[i][n])

# print(dp)
if dp[M][2**N-1] == 10**10:
  ans = -1
else:
  ans = dp[M][2**N-1]

print(ans)