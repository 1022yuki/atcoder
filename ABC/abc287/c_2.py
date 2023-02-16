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

# 各次数が正しいかチェック
jisu = []
for i in range(N):
  jisu.append(len(edges[i]))

jisu.sort()
cor_jisu = [1]*2+[2]*(N-2)
# print(jisu)
# print(cor_jisu)
if jisu != cor_jisu:
  print("No")
  exit()

    
visited = [False]*N
# dfsして全部visitedになるかチェック
def dfs(i):
  visited[i] = True
  for j in edges[i]:
    if not visited[j]:
      dfs(j)

dfs(0)

for i in range(N):
  if not visited[i]:
    print("No")
    exit()

print("Yes")