from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

X = []
for i in range(Q):
  X.append(int(input()))

A.sort()

for x in X:
  ans = bisect_left(A, x)
  print(ans)