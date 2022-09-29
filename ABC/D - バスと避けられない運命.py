N, M = map(int, input().split())

inf = 10**100
dist = []
for i in range(N):
  dist.append([inf]*N)
for i in range(N):
  dist[i][i] = 0

for i in range(M):
  a, b, t = map(int, input().split())
  a -= 1
  b -= 1
  dist[a][b] = t
  dist[b][a] = t

for k in range(N):
  for x in range(N):
    for y in range(N):
      dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])

# for i in range(N):
#   print(dist[i])

m_list = []
for i in range(N):
  m_list.append(max(dist[i]))

ans = min(m_list)
print(ans)  