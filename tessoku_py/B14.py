N, K = map(int, input().split())
A = list(map(int, input().split()))

B = []
C = []
for i in range(N):
  if i%2==0:
    B.append(A[i])
  else:
    C.append(A[i])

def has_bit(n, i):
  return n & (1<<i) > 0

from collections import defaultdict

dic = defaultdict(int)

for n1 in range(1<<(len(B))):
  sum1 = 0
  for i in range(len(B)):
    if has_bit(n1, i):
      sum1 += B[i]
  dic[sum1] += 1

# print(B)
# print(C)
# print(dic)

for n2 in range(1<<(len(C))):
  sum2 = 0
  for j in range(len(C)):
    if has_bit(n2, j):
      sum2 += C[j]
  print(sum2)
  if dic[K-sum2] != 0:
    print('Yes')
    exit()

print('No')