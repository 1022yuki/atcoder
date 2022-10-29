from re import I


W, H = map(int, input().split())

mod = 10**9+7

a = 1
b = 1
for i in range(2, W+H-1):
  a *= i
  a %= mod
for i in range(2, W):
  b *= i
  b %= mod
for i in range(2, H):
  b *= i
  b %= mod

# 繰り返し2乗法によりa^bを高速に計算(modを取りながら)
# def power(a, b, mod):
#   answer = 1
#   for i in range(30):
#     bit = b % 2
#     b = b // 2
#     if bit == 1:
#       answer *= a**(2**i)
#       answer %= mod
#   return answer

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

ans = (a*power(b,mod-2, mod)) % mod
print(ans)