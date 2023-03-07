import bisect
from collections import defaultdict
H, W, rs, cs = map(int, input().split())
N = int(input())

rs -= 1
cs -= 1

R = defaultdict(list)
C = defaultdict(list)
for i in range(N):
  r, c = map(int, input().split())
  r -= 1
  c -= 1
  R[r].append(c)
  C[c].append(r)

for item in R.values():
  item.append(-1)
  item.append(W)
  item.sort()

for item in C.values():
  item.append(-1)
  item.append(H)
  item.sort()

Q = int(input())
D = []
L = []
for i in range(Q):
  d, st_l = map(str, input().split())
  l = int(st_l)
  D.append(d)
  L.append(l)

for i in range(Q):
  dir = D[i]
  l = L[i]

  if dir == "L":
    if rs in R:
      use_li = R[rs]
    else:
      use_li = [-1, W]
    bis_be = bisect.bisect_left(use_li, cs)
    bis_af = bisect.bisect_left(use_li, cs-l)
    if bis_be == bis_af:
      cs -= l
    else:
      cs = use_li[bis_be-1]+1

  if dir == "R":
    if rs in R:
      use_li = R[rs]
    else:
      use_li = [-1, W]
    bis_be = bisect.bisect_right(use_li, cs)
    bis_af = bisect.bisect_right(use_li, cs+l)
    if bis_be == bis_af:
      cs += l
    else:
      cs = use_li[bis_be]-1

  if dir == "U":
    if cs in C:
      use_li = C[cs]
    else:
      use_li = [-1, H]
    bis_be = bisect.bisect_left(use_li, rs)
    bis_af = bisect.bisect_left(use_li, rs-l)
    if bis_be == bis_af:
      rs -= l
    else:
      rs = use_li[bis_be-1]+1

  if dir == "D":
    if cs in C:
      use_li = C[cs]
    else:
      use_li = [-1, H]
    bis_be = bisect.bisect_right(use_li, rs)
    bis_af = bisect.bisect_right(use_li, rs+l)
    if bis_be == bis_af:
      rs += l
    else:
      rs = use_li[bis_be]-1

  print(rs+1, cs+1)