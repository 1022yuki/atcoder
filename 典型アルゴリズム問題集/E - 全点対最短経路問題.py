INF = 10**100

N, M = map(int, input().split())

dist = []
for i in range(N):
  dist.append([INF]*N)

# print(dist)

for i in range(N):
  dist[i][i] = 0

for i in range(M):
  u, v, c = map(int, input().split())
  dist[u][v] = c

# print(dist)

for k in range(N):
  for x in range(N):
    for y in range(N):
      dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])

# print(dist)

sum = 0
for i in range(N):
  for j in range(N):
    sum += dist[i][j]

print(sum)