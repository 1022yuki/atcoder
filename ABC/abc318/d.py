N = int(input())

# 隣接行列
edges = []
for i in range(N):
  edges.append([-1]*N)
edge_num = []

for i in range(N-1):
  d = list(map(int, input().split()))
  for j in range(len(d)):
    edges[i][i+j+1] = d[j]
    edges[i+j+1][i] = d[j]
    edge_num.append([i, i+j+1])

def has_bit(n, i):
  return (n & (1<<i) > 0)

# bitDP
dp = []
for i in range((N*(N-1)//2)+1):
  dp.append([-1]*(2**N))

dp[0][0] = 0

for i in range(N*(N-1)//2):
  v_i, v_j = edge_num[i]
  for n in range((2**N)):
    if dp[i][n]==-1:
      continue
    # 使わない
    dp[i+1][n] = max(dp[i+1][n], dp[i][n])
    if has_bit(n, v_i) or has_bit(n, v_j):
      continue
    # 辺iを使う
    dp[i+1][n|(1<<v_i)|(1<<v_j)] = max(dp[i+1][n|(1<<v_i)|(1<<v_j)], dp[i][n]+edges[v_i][v_j])

print(max(dp[N*(N-1)//2]))