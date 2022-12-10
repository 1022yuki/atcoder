def has_bit(n, i):
  return n & 1<<i > 0

# a の b 乗を m で割った余りを返す関数
def power(a, b, m):
  p = a
  Answer = 1
  # rangeの部分はb<2**rangeになるように調整
  for i in range(30):
    if has_bit(b, i):
      # bitが立っていたら答えにpを掛けてmで割る
      Answer = (Answer*p) % m
    # pはa^2, a^4, a^8,...
    p = (p * p) % m
  return Answer

a, b = map(int, input().split())

print(power(a, b, 1000000007))