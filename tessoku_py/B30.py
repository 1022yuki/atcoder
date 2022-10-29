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


H, W = map(int, input().split())

mod = 10**9 + 7

a = 1
for i in range(2, H+W-1):
  a *= i
  a %= mod

b = 1
for i in range(2, H):
  b *= i
  b %= mod
for i in range(2, W):
  b *= i
  b %= mod

ans = (a*power(b, mod-2, mod)) % mod
print(ans)