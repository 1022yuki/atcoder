import heapq

N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b, c = map(int, input().split())
  edges[a].append([c, b])
  edges[b].append([c, a])

# print(edges)

dist = [-1]*(N+1)
dist[1] = 0

done = [False] * (N+1)

Q = []

heapq.heappush(Q, (0, 1))

while len(Q)>0:
  d, i = heapq.heappop(Q)

  # print(d, i)

  if done[i]:
    continue

  done[i] = True

  for (c, j) in edges[i]:
    if dist[j] == -1  or dist[j] > dist[i] + c:
      dist[j] = dist[i] + c
      heapq.heappush(Q, (dist[j], j))

# print(dist)

for i in range(1, N+1):
  print(dist[i])