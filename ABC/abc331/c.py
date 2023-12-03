N = int(input())
A = list(map(int, input().split()))

sorted_A = sorted(A)
import bisect

sum = [0]
for i in range(N):
  sum.append(sum[i]+sorted_A[i])

for i in range(N):
  idx = bisect.bisect_right(sorted_A, A[i])
  print(sum[-1]-sum[idx], end=" ")