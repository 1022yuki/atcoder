N, Q = map(int, input().split())
C = list(map(int, input().split()))

qs = []
for i in range(Q):
  qs.append(list(map(int, input().split())))

Bs = []
for i in range(N):
  Bs.append(set())
for i in range(N):
  Bs[i].add(C[i])

# print(Bs)

for i in range(Q):
  a, b = qs[i]
  if len(Bs[a-1]) < len(Bs[b-1]):
    for c in Bs[a-1]:
      Bs[b-1].add(c)
    Bs[a-1] = set()
  else:
    for c in Bs[b-1]:
      Bs[a-1].add(c)
    Bs[b-1] = Bs[a-1]
    Bs[a-1] = set()

  # print(Bs)
  print(len(Bs[b-1]))