import sys
sys.setrecursionlimit(10**7)
from collections import deque

N, X, Y = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])

for i in range(N-1):
  u, v = map(int, input().split())
  edges[u].append(v)
  edges[v].append(u)

# print(edges)

st = deque()
visited = [False]*(N+1)


def rec(i):
  if visited[Y]:
    print(*st)

    exit()
  for j in edges[i]:
    if not visited[j]:
      visited[j] = True
      st.append(j)
      rec(j)
      st.pop()

st.append(X)
visited[X] = True

rec(X)