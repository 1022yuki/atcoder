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

visited = [False]*N
cnt = 0

# path = []

def dfs(i):
  global cnt
  visited[i] = True
  # path.append(i)
  for j in edges[i]:
    if not visited[j]:
      dfs(j)
  flag = True
  for k in range(N):
    if not visited[k]:
      flag = False
  if flag:
    cnt += 1
    # print(path)
  visited[i] = False
  # path.pop()

dfs(0)

print(cnt)