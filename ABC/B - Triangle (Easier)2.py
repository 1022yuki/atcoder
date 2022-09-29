N, M = map(int, input().split())

edge = []
for _ in range(N):
  edge.append([False]*N)

for _ in range(M):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  edge[u][v] = True
  edge[v][u] = True

count = 0
for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      if edge[i][j] and edge[j][k] and edge[k][i]:
        count += 1

print(count)