N, M = map(int, input().split())

# 2進数→10進数へ変換
# 引数は文字列型を想定
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
  inp = list(map(str, input().split()))
  bin = "".join(inp)
  num = from_bin(bin)
  coupon.append(num)

# print(coupon)

dp = []
for i in range(M+1):
  dp.append([100]*(2**N))

dp[0][0] = 0

for i in range(M):
  for b_num in range(2**N):
    dp[i+1][b_num] = min(dp[i+1][b_num], dp[i][b_num])
    dp[i+1][b_num|coupon[i]] = min(dp[i+1][b_num|coupon[i]], dp[i][b_num]+1)

if dp[M][2**N-1] == 100:
  print(-1)
else:
  print(dp[M][2**N-1])