N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

from collections import defaultdict
dic = defaultdict(int)

for i in range(N):
  dic[A[i]] += 1

for i in range(N):
  if dic[A[i]+X] != 0:
    print('Yes')
    exit()

print('No')