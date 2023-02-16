N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  edges[u].append(v)
  edges[v].append(u)

# print(edges)

import sys
sys.setrecursionlimit(10**8)

visited = [False]*N

limit = 10**6
cnt = 0

def dfs(i):
  global cnt
  cnt += 1
  if cnt == limit:
    print(cnt)
    exit()
    # return
  visited[i] = True
  for j in edges[i]:
    if not visited[j]:
      dfs(j)
  visited[i] = False

dfs(0)
print(cnt)