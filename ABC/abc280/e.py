N, P = map(int, input().split())

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
# dp[i]:
dp = [None]*(N+1)
dp[0] = 0
dp[1] = 1
# dp[2] = P/100+(1-P/100)*2
for i in range(2, N+1):
  # dp[i] = (P/100)*(dp[i-2]+1) + (1-P/100)*(dp[i-1]+1)
  # dp[i] = ((P*power(100, mod-2, mod))*(dp[i-2]+1) + ((100-P)*power(100, mod-2, mod))*(dp[i-1]+1))%mod
  bunnsi = P*dp[i-2] + (100-P)*dp[i-1]+100
  bunnbo = 100
  dp[i] = (bunnsi*power(bunnbo, mod-2, mod))%mod

print(dp[N]%mod)