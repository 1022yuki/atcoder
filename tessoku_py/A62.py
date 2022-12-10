import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

edges = []
for i in range(N+1):
  edges.append([])
for i in range(M):
  a, b = map(int, input().split())
  edges[a].append(b)
  edges[b].append(a)

visited = [False]*N

def rec(i):
  visited[i-1] = True
  for x in edges[i]:
    if not visited[x-1]:
      rec(x)

rec(1)
# print(edges)
# print(visited)

state = True
for flag in visited:
  if not flag:
    state = False

if state:
  print('The graph is connected.')
else:
  print('The graph is not connected.')