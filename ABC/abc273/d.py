from bisect import bisect_left


H, W, rs, cs = map(int, input().split())
N = int(input())
R = []
C = []
for i in range(N):
  r, c = map(int, input().split())
  R.append(r)
  C.append(c)
Q = int(input())
D = []
L = []
for i in range(Q):
  d, l = map(str, input().split())
  D.append(d)
  L.append(int(l))

# grid = []
# grid.append([0]*(W+1))
# for i in range(H):
#   grid.append([0]+['.']*W)

# for i in range(N):
#   r = R[i]
#   c = C[i]
#   grid[r][c] = '#'

# print(grid)

wl = [[0]]
wc = [[0]]

for i in range(H):
  li = [0]
  wl.append(li)
for i in range(W):
  li = [0]
  wc.append(li)

for i in range(N):
  r = R[i]
  c = C[i]
  wl[r].append(c)
  wc[c].append(r)

for i in range(1, H+1):
  wl[i].append(H+1)
for i in range(1, W+1):
  wc[i].append(W+1)

# print(wl)
# print(wc)

# print(rs)
# print(cs)
op = []

for i in range(Q):
  di = D[i]
  li = L[i]

  if di == 'L':
    use_li = wl[rs]
    # print(use_li)
    bis = bisect_left(use_li, cs)
    if cs - use_li[bis-1] -1 >= li:
      cs -= li
    else:
      cs -= cs - use_li[bis-1] -1
    op.append((rs, cs))

  if di == 'R':
    use_li = wl[rs]
    # print(use_li)
    bis = bisect_left(use_li, cs)
    # print(bis)
    # print(use_li[bis+1] - cs -1)
    if use_li[bis] - cs -1 >= li:
      cs += li
    else:
      cs += use_li[bis] - cs -1
    op.append((rs, cs))

  if di == 'U':
    use_li = wc[cs]
    # print(use_li)
    bis = bisect_left(use_li, rs)
    if rs - use_li[bis-1] -1 >= li:
      rs -= li
    else:
      rs -= rs - use_li[bis-1] -1
    op.append((rs, cs))

  if di == 'D':
    use_li = wc[cs]
    # print(use_li)
    bis = bisect_left(use_li, rs)
    if use_li[bis] - rs -1 >= li:
      rs += li
    else:
      rs += use_li[bis] - rs -1
    op.append((rs, cs))

# print(op)

for i in range(Q):
  i, j = op[i]
  print(str(i)+' '+str(j))