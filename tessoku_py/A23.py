N, M = map(int, input().split())

inf = 10**9

def from_bin(s: str) -> int:
  leng = len(s)
  ans = 0
  for i in range(leng):
    if s[leng-1-i] == '1':
      kurai = 1<<i
      ans += kurai
  return ans

coupon = []
for i in range(M):
  li = list(map(str, input().split()))
  bin = "".join(li)
  coupon.append(from_bin(bin))

# print(coupon)

# def has_bit(n, i):
#   return n & (1<<i) > 0

dp = []
for i in range(M+1):
  dp.append([inf]*(2**N))
dp[0][0] = 0

# print(dp)

for i in range(M):
  for n in range(2**N):
    dp[i+1][n] = min(dp[i+1][n], dp[i][n])
    # print(n)
    # print(coupon[i])
    # print(n|coupon[i])
    dp[i+1][n|coupon[i]] = min(dp[i+1][n|coupon[i]], dp[i][n]+1)

ans = dp[M][(1<<N)-1]
if ans == inf:
  print(-1)
else:
  print(ans)