N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

# print(edges)

friends = 0
for i in range(1, N+1):
  friends = max(friends, len(edges[i]))
  if friends == len(edges[i]):
    ans = i

print(ans)