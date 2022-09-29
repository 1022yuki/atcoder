from collections import deque

N, M = map(int, input().split())

edges = [[] for _ in range(N)]


for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append(b)
  edges[b].append(a)

Q = deque()
Q.append(0)

dist = [-1] * N
dist[0] = 0

while(len(Q)>0):
  i = Q.popleft()

  for j in edges[i]:
    if dist[j] == -1:
      dist[j] = dist[i] + 1
      Q.append(j)

# print(dist)

if dist[-1] == 2:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')