import sys
sys.setrecursionlimit(10**7)
import pypyjit
pypyjit.set_param('max_unroll_recursion=0') 

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])

for i in range(M):
  a, b, x, y = map(int, input().split())
  a -= 1
  b -= 1
  edges[a].append((b, x, y))
  x *= -1
  y *= -1
  edges[b].append((a, x, y))

coord = []
for i in range(N):
  coord.append([])
coord[0] = (0, 0)

def dfs(i, x, y):
  coord[i] = (x, y)
  for j, dx, dy in edges[i]:
    if coord[j]==[]:
      dfs(j, x+dx, y+dy)

dfs(0, 0, 0)

for i in range(N):
  if len(coord[i]) == 0:
    print("undecidable")
  else:
    print(coord[i][0], coord[i][1])