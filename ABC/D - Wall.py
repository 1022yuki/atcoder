H, W = map(int, input().split())

dist = []
for i in range(10):
  C = list(map(int, input().split()))
  dist.append(C)

for k in range(10):
  for x in range(10):
    for y in range(10):
      dist[x][y] = min(dist[x][y], dist[x][k]+dist[k][y])

# for i in range(10):
#   print(dist[i][1])

A = []
for i in range(H):
  a = list(map(int, input().split()))
  A.append(a)

sum = 0
for i in range(H):
  for j in range(W):
    for num in range(10):
      if A[i][j] == num:
        sum += dist[num][1]
        break

print(sum)