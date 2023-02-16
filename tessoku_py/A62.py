import sys
sys.setrecursionlimit(10**6)

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

visited = [False]*N

def rec(i):
  visited[i] = True
  for x in edges[i]:
    if not visited[x]:
      rec(x)

rec(0)

state = True
for flag in visited:
  if not flag:
    state = False
    break

if state:
  print('The graph is connected.')
else:
  print('The graph is not connected.')