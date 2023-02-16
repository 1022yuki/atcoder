N, M = map(int, input().split())
edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append(b)
  edges[b].append(a)
# print(edges)

import sys
sys.setrecursionlimit(10**7)
from collections import deque

Q = deque()

visited = [False]*N
def rec(i):
  visited[i] = True
  Q.append(i)
  if i == N-1:
    for i in Q:
      print(i+1, end=" ")
    print()
    return
  for j in edges[i]:
    if not visited[j]:
      rec(j)
      Q.pop()

rec(0)