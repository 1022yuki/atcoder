import sys
sys.setrecursionlimit(10**6)
from collections import deque

N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

visited = [False]*(N+1)

Q = deque()

def rec(i):
  Q.append(i)
  if i == N:
    print(*list(Q))
    exit()
  visited[i] = True
  for x in edges[i]:
    if not visited[x]:
      rec(x)
      Q.pop()

rec(1)