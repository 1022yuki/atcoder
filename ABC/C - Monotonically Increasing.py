N , M = map(int, input().split())

import itertools

n = []
for i in range(M):
  n.append(i+1)

c = itertools.combinations(n, N)

for v in c:
  print(*v)