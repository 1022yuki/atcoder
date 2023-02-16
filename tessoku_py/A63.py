from collections import deque

N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

dist = [-1]*(N+1)
dist[1] = 0

Q = deque()
Q.append(1)

while len(Q)>0:
  i = Q.popleft()
  for x in edges[i]:
    if dist[x] == -1:
      dist[x] = dist[i] + 1
      Q.append(x)

for i in range(1, N+1):
  print(dist[i])