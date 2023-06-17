N, A, B, P, Q = map(int, input().split())

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

mod = 998244353

# dp[i][j][k]: iターン終了後k君がjにいる確率
dp = []
for i in range(N):
  dp.append([])
  for j in range(N+1):
    dp[i].append([0, 0])

dp[0][A][0] = 1
dp[0][B][1] = 1

ans = 0

for i in range(1, N):
  for j in range(1, N):
    for p in range(1, P+1):
      dp[i][min(N, j+p)][0] += (dp[i-1][j][0]*power(P, mod-2, mod))%mod
    for q in range(1, Q+1):
      dp[i][min(N, j+q)][1] += (dp[i-1][j][1]*power(Q, mod-2, mod))%mod
  # iターン目終了後
  for k in range(1, N):
    ans += (dp[i][N][0]*dp[i-1][k][1])%mod

# print(dp)
print(ans%mod)

# print(2*power(3, mod-2, mod))