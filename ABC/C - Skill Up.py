N, M, X = map(int, input().split())

C = []
A = []
for i in range(N):
  li = list(map(int, input().split()))
  c = li[0]
  li_A = li[1:]
  C.append(c)
  A.append(li_A)

ALL = 1<<N

def has_bit(n, i):
  return n & (1<<i) > 0

ans = 10**100

for n in range(ALL):
  cost = 0
  comp = [0]*M
  for book in range(N):
    if has_bit(n, book):
      cost += C[book]
      for i in range(M):
        comp[i] += A[book][i]
  # print(comp)
  state = True
  for x in comp:
    if x < X:
      state = False
      break
  if state:
    ans = min(ans, cost)

if ans != 10**100:
  print(ans)
else:
  print(-1)