X, Y = map(int, input().split())

mod = 10**9+7

ans_a = -1
ans_b = -1

if (2*X-Y)%3==0 and 2*X-Y>=0:
  if (2*Y-X)%3==0 and 2*Y-X>=0:
    ans_a = (2*Y-X) // 3
    ans_b = (2*X-Y) // 3
# for a in range(1, 10**6):
#   b1 = X-2*a
#   b2 = (Y-a)/2
#   if b1>0 and b1==b2:
#     ans_a = a
#     ans_b = b1

# print(ans_a, ans_b)
    

if ans_a == -1 and ans_b == -1:
  print(0)
  exit()

s = 1
t = 1

for i in range(2, ans_a+ans_b+1):
  s *= i
  s%=mod
for i in range(2, ans_a+1):
  t *= i
  t%=mod
for i in range(2, ans_b+1):
  t *= i
  t%=mod

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

ans = (s*power(t, mod-2, mod)) % mod
print(ans)