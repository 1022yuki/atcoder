N = int(input())
A = list(map(int, input().split()))

edges = []
for i in range(2*N+1):
  edges.append([])
for i in range(N):
  edges[A[i]-1].append(2*i+1)
  edges[A[i]-1].append(2*i+2)

# print(edges)

dist = [-1]*(2*N+1)
dist[0] = 0

from collections import deque

Q = deque()

Q.append(0)

while(len(Q)>0):
  i = Q.popleft()
  # print(i)
  for ni in edges[i]:
    if dist[ni]==-1:
      dist[ni] = dist[i]+1
      Q.append(ni)

# print(dist)
for i in range(2*N+1):
  print(dist[i])