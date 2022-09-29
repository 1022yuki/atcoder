N, X, Y = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(N-1):
  u, v = map(int, input().split())
  edges[u-1].append(v-1)
  edges[v-1].append(u-1)

# print(edges)

visited = [False] * N

import sys
sys.setrecursionlimit(1000000)

flag = False
road = []

def dfs(i):
  # print(i)
  global flag
  visited[i] = True
  if i == Y-1:
    flag = True
    # print(i+1)
    road.append(i)
    
  # if not flag:
  for j in edges[i]:
    if not visited[j] and flag == False:
      dfs(j)
      if flag:
        # print(i+1)
        road.append(i)
        


dfs(X-1)

# print(road)

length = len(road)
for i in range(length-1, -1, -1):
  print(road[i]+1, end=' ')
print()