N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

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

# dp[i]: iマス目から始めた時の期待値
# 答えはdp[0]
dp = [-1]*(N+1)
# 初期値
dp[N] = 0

sumP = 0
sumA = 0
for i in range(N-1, -1, -1):
  sumA += A[i]
  dp[i] = (sumP+sumA)*power(N, MOD-2, MOD)
  dp[i] %= MOD
  sumP += dp[i]

# print(dp)
print(dp[0])