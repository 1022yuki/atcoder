N, M, K = map(int, input().split())

mod = 998244353
inf = 10**10

def has_bit(n, i):
  return n & 1<<i > 0

# a の b 乗を m で割った余りを返す関数
def power(a, b, m):
  p = a
  Answer = 1
  # rangeの部分はb<2**rangeになるように調整
  for i in range(30):
    if has_bit(b, i):
      Answer = (Answer*p) % m
    p = (p * p) % m
  return Answer

# dp[k][i]: ルーレットをk回回した後にマスiにいる確率
# 遷移はM通り
dp = []
for i in range(K+1):
  dp.append([0]*(N+1))
dp[0][0] = 1

pow = power(M, mod-2, mod)

for k in range(K):
  for i in range(N):
    if dp[k][i]==0:
      continue
    for m in range(1, M+1):
      if i+m<=N:
        next = i+m
      else:
        next = 2*N-i-m
      dp[k+1][next] = dp[k+1][next]+dp[k][i]*pow
      dp[k+1][next] %= mod

# print(dp)

# 答えはdp[k][N]の和
ans = 0
for k in range(K+1):
  ans += dp[k][N]
  ans %= mod

print(ans)