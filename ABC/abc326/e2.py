N = int(input())
A = list(map(int, input().split()))

# 期待値DP
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


# マスnを踏む確率
dp = [0]*(N+1)
sum = 1

for i in range(1, N+1):
  dp[i] = sum * power(N, MOD-2, MOD)
  dp[i] %= MOD
  sum += dp[i]
# print(dp)

# マスnを踏む確率*A[i]を足し合わせる
ans = 0
for i in range(1, N+1):
  ans += dp[i]*A[i-1]
  ans %= MOD
print(ans)