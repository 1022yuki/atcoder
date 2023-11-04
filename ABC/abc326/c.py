N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

import bisect
ans = 0
for i in range(N):
  ind = bisect.bisect_left(A, A[i]+M)
  ans = max(ans, ind-i)

print(ans)