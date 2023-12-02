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

N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

# dp[i]: マスiにいる状態からゴールするまでにサイコロを振る回数の期待値
dp = [-1]*(N+1)
dp[N] = 0
done = [False]*(N+1)
done[N] = True

