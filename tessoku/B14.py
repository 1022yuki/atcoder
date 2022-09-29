from collections import defaultdict


N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
C = []
for i in range(N):
  if i % 2 == 0:
    B.append(A[i])
  else:
    C.append(A[i])

def has_bit(n, i):
  return n & 1<<i > 0

dict = defaultdict(int)

for n in range(1<<len(B)):
  sum = 0
  for i in range(len(B)):
    if has_bit(n, i):
      sum += B[i]
  dict[sum] += 1

ans = 0
for n in range(1<<len(C)):
  sum = 0
  for i in range(len(C)):
    if has_bit(n, i):
      sum += C[i]
  ans += dict[K-sum]

if ans >= 1:
  print('Yes')
else:
  print('No')