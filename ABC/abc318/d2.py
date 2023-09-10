N = int(input())

# 隣接リスト
edges = []
for i in range(N):
  edges.append([-1]*N)

for i in range(N-1):
  D = list(map(int, input().split()))
  for j in range(len(D)):
    edges[i][i+j+1] = D[j]
    edges[i+j+1][i] = D[j]

def has_bit(n, i):
  return (n & (1<<i) > 0)

dp = []
inf = 10**2
for i in range(N+1):
  dp.append([inf*-1]*(2**N))
dp[0][0] = 0

for i in range(N):
  for n in range(2**N):
    if has_bit(n, i):
      continue
    # 頂点iを使わない場合
    dp[i+1][n] = max(dp[i+1][n], dp[i][n])
    # 頂点iを使う場合
    for j in range(N):
      if has_bit(n, j):
        continue
      dp[i+1][n|(1<<i)|(1<<j)] = max(dp[i+1][n|(1<<i)|(1<<j)], dp[i][n]+edges[i][j])

ans = max(dp[N])
print(ans)