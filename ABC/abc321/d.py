N, M, P = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# 累積和
sum_B = [0]
for i in range(M):
  sum_B.append(sum_B[-1]+B[i])

ans = 0

import bisect

for a in A:
  # Bを二分探索
  # aとbの和がP以下になるか
  ok = bisect.bisect_left(B, P-a)
  # okの分はa+bをansにたす
  ans += a*(ok)
  ans += sum_B[ok]
  # ngの分はPをng個分たす
  ans += P*(M-ok)

print(ans)