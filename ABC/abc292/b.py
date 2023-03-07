N, Q = map(int, input().split())

from collections import defaultdict

dic = defaultdict(int)
qs = []
for i in range(Q):
  inp = list(map(int, input().split()))
  qs.append(inp)

for i in range(Q):
  q = qs[i]
  x = q[1]
  if q[0] == 1:
    dic[x] += 1
  if q[0] == 2:
    dic[x] += 2
  if q[0] == 3:
    if dic[x]>=2:
      print("Yes")
    else:
      print("No")