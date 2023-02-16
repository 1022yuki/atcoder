import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())

edges = []
for i in range(N):
  edges.append([])
for i in range(M):
  u, v = map(int, input().split())
  u-=1
  v-=1
  edges[u].append(v)
  edges[v].append(u)

for i in range(N):
  if len(edges[i]) > 2:
    print("No")
    exit()

visited = [False]*N

def dfs(i, pre):
  # print(i)
  visited[i] = True
  for j in edges[i]:
    if visited[j] and j != pre:
      print("No")
      exit()
    if not visited[j]:
      dfs(j, i)

dfs(0, -1)

# print(visited)

for i in range(N):
  if not visited[i]:
    print("No")
    exit()

print("Yes")