N = int(input())
Q = int(input())

qs = []
for i in range(Q):
  q = list(map(str, input().split()))
  qs.append(q)

c_li = []
for i in range(N):
  c_li.append([])

from collections import defaultdict
dic = defaultdict((set))

for i in range(Q):
  q = qs[i]
  if q[0]=="1":
    i, j = int(q[1]), int(q[2])
    c_li[j-1].append(i)
    dic[i].add(j)

  if q[0]=="2":
    i = int(q[1])
    box = c_li[i-1]
    # u_b = list(set(box))
    box.sort()
    print(*box)

  if q[0]=="3":
    i = int(q[1])
    box = dic[i]
    u_b = list(box)
    u_b.sort()
    print(*u_b)