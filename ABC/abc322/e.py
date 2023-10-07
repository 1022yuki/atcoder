N, K, P = map(int, input().split())

INF = 10**13

Costs = []
Params = []
for i in range(N):
  inp = list(map(int, input().split()))
  Costs.append(inp[0])
  Params.append(inp[1:])

dp = []
for i in range(N+1):
  dp.append([INF]*((P+1)**K))
dp[0][0] = 0

# n進数の数numのk桁目の値を返す
def get_num(n, num, k):
  return (num//(n**k))%n

def to_k(k, num):
  res = []
  while num > 0:
    res.append(num%k)
    num //= k
  return res

# print(get_num(2, 5, 0))
# print(get_num(2, 5, 1))
# print(get_num(2, 5, 2))

for i in range(N):
  cost = Costs[i]
  params = Params[i]
  # print(cost, params)
  for j in range((P+1)**K):
    if dp[i][j] == INF:
      continue
    # print(to_k(P+1, j))
    # iこ目の商品を使わない場合
    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    # iこ目の商品を使う場合
    new_ind = j
    for k in range(K):
      dig_num = min(get_num(P+1, j, k)+params[k], P)
      new_ind += (dig_num-get_num(P+1, j, k))*((P+1)**k)
    dp[i+1][new_ind] = min(dp[i+1][new_ind], dp[i][j]+cost)
    # print(to_k(P+1, new_ind))

# print(dp)
print(dp[N][(P+1)**K-1]) if dp[N][(P+1)**K-1] != INF else print(-1)