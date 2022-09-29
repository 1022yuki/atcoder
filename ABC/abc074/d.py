import copy

N = int(input())

dist = []
for _ in range(N):
  dist.append(list(map(int, input().split())))


for i in range(N):
  dist[i][i] = 0

c_dist = copy.deepcopy(dist)

for k in range(N):
  for x in range(N):
    for y in range(N):
      dist[x][y] = min(dist[x][y], dist[x][k] + dist[k][y])

# print(dist)
# print(c_dist)

if dist != c_dist:
  print(-1)
  exit()

ans = 0
for x in range(N):
  for y in range(x+1, N):
    yorimiti = 10 ** 100
    for k in range(N):
      if k != x and k != y:
        yorimiti = min(yorimiti, dist[x][k] + dist[k][y])
    if yorimiti > dist[x][y]:
      ans += dist[x][y]

print(ans)