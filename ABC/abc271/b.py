N, Q = map(int, input().split())

L = []
for i in range(N):
  inp = list(map(int, input().split()))
  l = inp[0]
  a = inp[1:]
  L.append(a)

# print(L)

queries = []
for i in range(Q):
  s, t = map(int, input().split())
  queries.append([s, t])

# print(queries)

for i in range(Q):
  s, t = queries[i]
  print(L[s-1][t-1])